import pandas as pd
from ai.exercises.helpers import calculate_total, format_currency

# Read data
df = pd.read_csv("ai/data/sales.csv")

# Calculate total for each row
totals = []
for index, row in df.iterrows():
    total = calculate_total(row["quantity"], row["price"])
    totals.append(total)

# Add totals to our data
df["total"] = totals

# Display with formatted totals
print("Sales Data:")
for index, row in df.iterrows():
    formatted_total = format_currency(row["total"])
    print(f"{row['product']} total: {formatted_total}")

# Show grand total
grand_total = df["total"].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")
