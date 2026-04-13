import pandas as pd

# =========================
# FIXED COSTS
# =========================
LABEL_COST = 6
PACKING_COST = 5
PROFIT_MARGIN = 5
TOTAL_EXTRA = LABEL_COST + PACKING_COST + PROFIT_MARGIN

# =========================
# LOAD EXCEL
# =========================
file_name = "Own Record 1201-1299.xlsx"
df = pd.read_excel(file_name)

# =========================
# CALCULATE FINAL PRICE
# =========================
for index, row in df.iterrows():
    source_price = row["Source Price"]

    if pd.isna(source_price):
        continue

    try:
        # Convert to float in case it's string
        source_price = float(source_price)
        df.at[index, "Source Price"] = round(source_price + TOTAL_EXTRA, 2)
    except ValueError:
        print(f"⚠️ Skipping row {index} because Source Price is not a number: {source_price}")

# =========================
# SAVE OUTPUT
# =========================
df.to_excel("output.xlsx", index=False)
print("DONE ✅ Source Price updated with final prices")
