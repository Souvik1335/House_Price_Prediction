import pandas as pd


def create_engineered_features(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df["Area_per_Bedroom"] = (
        df["Area_sqft"] / df["Bedrooms"]
    )

    df["Bathroom_per_Bedroom"] = (
        df["Bathrooms"] / df["Bedrooms"]
    )

    return df