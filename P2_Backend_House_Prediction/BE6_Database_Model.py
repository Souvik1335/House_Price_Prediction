from datetime import datetime
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from P2_Backend_House_Prediction.BE5_User_Database import Base, engine



# USER TABLE
class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )

    personal_phone = Column(
        String(15),
        unique=True,
        index=True,
        nullable=False
    )

    alternate_phone = Column(
        String(15),
        nullable=True
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    date_of_birth = Column(
        Date,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    # Relationship with PredictionHistory
    predictions = relationship(
        "PredictionHistory",
        back_populates="user",
        cascade="all, delete-orphan"
    )


# PREDICTION HISTORY TABLE
class PredictionHistory(Base):
    __tablename__ = "prediction_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    area_sqft = Column(
        Float,
        nullable=False
    )

    bedrooms = Column(
        Integer,
        nullable=False
    )

    bathrooms = Column(
        Integer,
        nullable=False
    )

    predicted_price = Column(
        Float,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # Relationship with User
    user = relationship(
        "User",
        back_populates="predictions"
    )

# Create database tables
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

    print("✅ Database tables created successfully")