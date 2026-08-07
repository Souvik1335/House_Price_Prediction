from M1_House_Price_Data import df
from M1_1_Feature_Engineering import create_engineered_features

# Delete House ID column
df = df.drop(columns=["HouseID"])

# Apply Feature Engineering
df = create_engineered_features(df)

# Separate features and target
X = df.drop(columns=["Price"])
y = df["Price"]

print(X.head())
print(X.columns)