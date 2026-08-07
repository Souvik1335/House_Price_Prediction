from M1_House_Price_Data import df


def create_engineered_features(df):

    df = df.copy()

    # Feature Engineering
    df["Area_per_Bedroom"] = df["Area_sqft"] / df["Bedrooms"]

    df["Bathroom_per_Bedroom"] = (
        df["Bathrooms"] / df["Bedrooms"]
    )

    return df


# Delete House ID column
df = df.drop(columns=["HouseID"])

# Apply Feature Engineering
df = create_engineered_features(df)


# Separate features and target
X = df.drop(columns=["Price"])
y = df["Price"]


print(X.head())
print(X.columns)