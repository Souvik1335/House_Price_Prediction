from pydantic import BaseModel, Field


class HousePricePrediction(BaseModel):

    Area_sqft: float = Field(gt=0)
    Bedrooms: int = Field(gt=0)
    Bathrooms: int = Field(gt=0)
    Floors: int = Field(gt=0)
    Age_of_House: int = Field(ge=0)
    Garage: int = Field(ge=0)
    Location_Score: float = Field(ge=0)
    Distance_to_City: float = Field(ge=0)
    School_Rating: float = Field(ge=0)
    Crime_Rate: float = Field(ge=0)