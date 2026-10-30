import pandas as pd

df = pd.read_csv("data/data.csv")

col = list(df.columns)

for i in col:
    print(i)

print(df["duration_minutes"].mean())

