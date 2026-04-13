import pandas as pd
import webbrowser
import time

df = pd.read_excel("Own Record 1201-1299.xlsx")

for i, row in df.iterrows():
    url = row["Store's URL"]

    if pd.isna(url):
        continue

    print(f"Opening link {i+1}")
    webbrowser.open(url)

    input("Close the tab, then press ENTER for next link...")
    time.sleep(1)

print("DONE ✅")
