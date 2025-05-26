import argparse
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_decision_links(index_url):
    """
    Scrape the index page to collect all decision URLs.
    """
    resp = requests.get(index_url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    links = []
    # adjust this selector if the site structure changes
    for a in soup.select('a[class*=decision]'):
        url = a.get('href', '')
        if url.startswith('https://www.oversightboard.com/decision/'):
            links.append(url)
    # dedupe
    return sorted(set(links))


def parse_decision(url):
    """
    Fetch and parse a single decision page, extracting metadata and body.
    Returns a dict with all desired fields.
    """
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')

    # Slug is the last segment of the URL
    slug = url.rstrip('/').split('/')[-1]
    # Title
    title_tag = soup.select_one('h1.entry-title') or soup.select_one('h1')
    title = title_tag.get_text(strip=True) if title_tag else ''

    # Metadata: dt/dd pairs
    meta = {}
    for dt, dd in zip(soup.select('dl dt'), soup.select('dl dd')):
        key = dt.get_text(strip=True).lower().replace(' ', '_')
        value = dd.get_text(strip=True)
        meta[key] = value

    # Summary: often in a summary section
    summary_tag = soup.select_one('.decision-summary p') or soup.select_one('.entry-content p')
    summary = summary_tag.get_text(strip=True) if summary_tag else ''

    # Body: all paragraphs after the summary (or in a specific content container)
    body_paragraphs = []
    for p in soup.select('.entry-content p'):
        text = p.get_text(strip=True)
        if text:
            body_paragraphs.append(text)
    body = "\n\n".join(body_paragraphs)

    # Compute lengths
    text_length = len(body)
    word_count = len(body.split())

    # Assemble row
    row = {
        'slug': slug,
        'title': title,
        'url': url,
        'summary': summary,
        'body': body,
        'text_length': text_length,
        'word_count': word_count,
    }
    # merge metadata fields
    row.update(meta)
    return row


def main(output_csv, delay):
    index_url = 'https://www.oversightboard.com/decision/'
    print(f"Fetching list of decisions from {index_url}...")
    links = get_decision_links(index_url)
    print(f"Found {len(links)} decision links.")

    rows = []
    for i, url in enumerate(links, 1):
        print(f"[{i}/{len(links)}] Scraping {url}")
        try:
            row = parse_decision(url)
            rows.append(row)
        except Exception as e:
            print(f"Error scraping {url}: {e}")
        time.sleep(delay)

    df = pd.DataFrame(rows)
    df.to_csv(output_csv, index=False)
    print(f"Wrote cleaned data to {output_csv}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scrape Oversight Board decisions into a CSV')
    parser.add_argument('output_csv', help='Path to write the enriched CSV')
    parser.add_argument('--delay', type=float, default=1.0,
                        help='Delay (in seconds) between requests')
    args = parser.parse_args()
    main(args.output_csv, args.delay)
