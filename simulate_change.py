import pandas as pd
df = pd.read_excel('live_data.xlsx')
if not df.empty:
    # Change a value to something that is definitely NOT what's on the web
    col = df.columns[1] # Usually 'Open'
    df.iloc[0, 1] = '000-0' 
    df.to_excel('live_data.xlsx', index=False)
    print(f"Changed {df.iloc[0, 0]} {col} to 000-0")
else:
    print("Excel is empty")
