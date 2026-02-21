# Reading a CSV file - needs exact path
import pandas as pd
import json, os
from pprint import pprint

print('현재 경로: ', os.path.abspath(os.curdir))
df = pd.read_csv("ai/data/sales.csv")
df['total'] = df['price'] * df['quantity']
# print(df)
print(f"Shape from csv : {df.shape[0]} rows, {df.shape[1]} columns\n")

df.to_json('ai/output/sales.json', orient='records', indent=2)
df.to_excel('ai/output/sales.xlsx', index=False)
df.to_csv('ai/output/sales.csv', index=False)

df = pd.read_json('ai/output/sales.json')
# print(df)

with open('ai/output/sales.json') as f:
    data = json.load(f)
    pprint(data, indent=2)