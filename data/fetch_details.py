# fetch_details.py

import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS    = {"User-Agent": "ResearchBot/1.0 (+your.email@example.com)"}
INPUT_CSV  = "decisions.csv"
OUTPUT_CSV = "decisions_enriched.csv"

# a simple regex matching "Month DD, YYYY"
DATE_RE = re.compile(r'^[A-Za-z]+ \d{1,2}, \d{4}$')

def fetch_decision_detail(url):
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    doc = BeautifulSoup(resp.text, "html.parser")
    
    # Restrict our search to the primary content area if possible
    main = doc.select_one('#primary') or doc

    # 1) Title: first <h1> on the page
    title_el = main.find('h1')
    title = title_el.get_text(strip=True) if title_el else ""

    # 2) Date: look for any text node matching MONTH DD, YYYY
    date = ""
    for txt in main.stripped_strings:
        if DATE_RE.match(txt):
            date = txt
            break

    # 3) Summary: the first <p> that isn’t the date
    summary = ""
    for p in main.find_all('p'):
        text = p.get_text(strip=True)
        if text and not DATE_RE.match(text):
            summary = text
            break

    # 4) Full text: concatenate all <p> under main
    paras = [p.get_text(strip=True) for p in main.find_all('p') if p.get_text(strip=True)]
    full_text = "\n\n".join(paras)

    return {
        "url":     url,
        "title":   title,
        "date":    date,
        "summary": summary,
        "text":    full_text
    }

def main():
    df = pd.read_csv(INPUT_CSV)
    records = []
    for idx, row in df.iterrows():
        print(f"Fetching {idx+1}/{len(df)}: {row.url}")
        det = fetch_decision_detail(row.url)
        det["slug"] = row.slug
        records.append(det)
    
    out = pd.DataFrame(records)
    out.to_csv(OUTPUT_CSV, index=False, encoding='utf-8')
    print(f"\n✅ Enriched data saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
