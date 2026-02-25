# Reading a CSV file - needs exact path
import pandas as pd
import json
import os
from pprint import pprint

# from pathlib import Path
# output_path_csv = Path("ai/data/weather.csv")
# output_path_csv.parent.mkdir(parents=True, exist_ok=True)

print("현재 경로: ", os.path.abspath(os.curdir))

# Ensure directories exist
os.makedirs("ai/data", exist_ok=True)
os.makedirs("ai/output", exist_ok=True)

df = pd.read_csv("ai/data/sales.csv")
df["total"] = df["price"] * df["quantity"]
# print(df)
print(f"Shape from csv : {df.shape[0]} rows, {df.shape[1]} columns\n")
print(df)

df.to_json("ai/output/sales.json", orient="records", indent=2)
df.to_excel("ai/output/sales.xlsx", index=False)
df.to_csv("ai/output/sales.csv", index=False)

df = pd.read_json("ai/output/sales.json")

with open("ai/output/sales.json") as f:
    data = json.load(f)
    # pprint(data, indent=2)
