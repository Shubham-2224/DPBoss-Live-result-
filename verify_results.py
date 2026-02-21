import pandas as pd
FILE_NAME = r"C:\Users\SHUBHAM\OneDrive\Desktop\dpboss live result\live_data.xlsx"
df = pd.read_excel(FILE_NAME)
print(df.head(20).to_string())
print("\nCheck for empty results:")
print(f"Total rows: {len(df)}")
print(f"Rows with Open empty: {df['Open'].isna().sum() + (df['Open'] == '').sum()}")
print(f"Rows with Main empty: {df['Main'].isna().sum() + (df['Main'] == '').sum()}")
