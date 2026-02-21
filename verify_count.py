from dpbosslive import scrape_data
df = scrape_data()
if df is not None:
    print(f"Total extracted: {len(df)}")
    print(df.tail(10))
else:
    print("Scrape failed")
