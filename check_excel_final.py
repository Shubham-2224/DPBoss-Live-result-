import pandas as pd
FILE_NAME = r"C:\Users\SHUBHAM\OneDrive\Desktop\dpboss live result\live_data.xlsx"
df = pd.read_excel(FILE_NAME, dtype=str).fillna("")
with open("excel_check.txt", "w") as f:
    for _, row in df.iterrows():
        if "PARVATI" in str(row["Name"]).upper() or "MAHADEVI" in str(row["Name"]).upper():
            f.write(f"{row['Name']} | Open: {row['Open']} | Main: {row['Main']} | Close: {row['Close']}\n")
