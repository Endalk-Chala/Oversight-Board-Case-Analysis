# clean_analysis_ready.py

import pandas as pd
import html
import re

# 1. Load your enriched dataset
df = pd.read_csv('decisions_enriched.csv', encoding='utf-8')

# 2. Keep only “real” decision slugs
df = df[df['slug'].str.match(r'^(bun|fb|ig|th)-')].copy()

# 3. Decode HTML entities in text fields
for col in ['title', 'summary', 'text']:
    if col in df.columns:
        df[col] = df[col].fillna('').apply(html.unescape)

# 4. Ensure a category column exists, then clean it
if 'category' not in df.columns:
    df['category'] = ''
else:
    df['category'] = df['category'].fillna('').apply(html.unescape)
df['category_clean'] = (
    df['category']
      .str.strip()
      .str.title()
      .replace('', 'Unknown')
)

# 5. Ensure an outcome column exists, then normalize it
if 'outcome' not in df.columns:
    df['outcome'] = ''
else:
    df['outcome'] = df['outcome'].fillna('').astype(str)
outcome_map = {
    'Upheld':           'Upheld',
    'Partially Upheld': 'Upheld',
    'Overturned':       'Overturned',
    'Modified':         'Modified'
}
df['outcome_norm'] = (
    df['outcome']
      .str.strip()
      .map(outcome_map)
      .fillna('Other')
)

# 6. Parse and standardize date
df['date'] = (
    df['date']
      .astype(str)
      .str.replace(r'Published on\s*', '', regex=True)
)
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['year']  = df['date'].dt.year
df['month'] = df['date'].dt.month

# 7. Compute text‐length
df['text_length'] = df['text'].fillna('').str.len()

# 8. Reorder columns for a clean layout
cols = [
    'slug', 'title', 'url',
    'date', 'year', 'month',
    'category', 'category_clean',
    'outcome', 'outcome_norm',
    'summary', 'text_length', 'text'
]
df = df[cols]

# 9. Save the clean, structured file
df.to_csv('decisions_clean_structured.csv', index=False, encoding='utf-8')
print(f"✅ Clean & structured data written to decisions_clean_structured.csv ({len(df)} rows)")
