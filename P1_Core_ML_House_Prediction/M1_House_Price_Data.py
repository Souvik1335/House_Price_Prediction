import pandas as pd

df = pd.read_csv("house_price_1k.csv")

print("Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nColumns:")
print(df.columns)