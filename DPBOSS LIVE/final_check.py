import pandas as pd
FILE_NAME = r"C:\Users\SHUBHAM\OneDrive\Desktop\dpboss live result\live_data.xlsx"
df = pd.read_excel(FILE_NAME, dtype=str).fillna("")
row = df[df['Name'] == 'PARVATI']
if not row.empty:
    print(f"PARVATI found:")
    print(f"Open: '{row['Open'].values[0]}'")
    print(f"Main: '{row['Main'].values[0]}'")
else:
    print("PARVATI not found")
