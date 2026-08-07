from pydantic import BaseModel, Field, EmailStr, model_validator
from datetime import date


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

# USER REGISTRATION

class UserRegistration(BaseModel):

    name: str = Field(min_length=2, max_length=100)

    email: EmailStr

    personal_phone: str = Field(
        min_length=10,
        max_length=15
    )

    alternate_phone: str | None = Field(
        default=None,
        min_length=10,
        max_length=15
    )

    password: str = Field(min_length=8)

    confirm_password: str = Field(min_length=8)

    date_of_birth: date

    @model_validator(mode="after")
    def check_passwords(self):

        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")

        return self