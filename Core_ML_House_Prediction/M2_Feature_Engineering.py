from M1_House_Price_Data import df

# Delete House ID column
df = df.drop(columns=['HouseID'])

# Feature Engineering
df['Area_per_Bedroom'] = df['Area_sqft'] / df['Bedrooms']

df['Bathroom_per_Bedroom'] = (df['Bathrooms'] / df['Bedrooms'])

# Separate features and target
X = df.drop(columns=["Price"])
y = df["Price"]

print(X.head())
print(X.columns)