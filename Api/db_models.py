from database import Base
import datetime
from sqlalchemy.sql import func
from sqlalchemy import (
    String,
    Integer,
    Float,
    Column, 
    DateTime
)


class Car(Base):
    __tablename__ = 'car_predictions'
    id = Column(Integer, primary_key=True, index=True)
    pred_time = Column(DateTime(timezone=True), default=func.now())
    powerPS = Column(Integer, default=0)
    vehicleType = Column(String(255))
    brand = Column(String(255))
    fuelType = Column(String(255))
    kilometer = Column(Float, default=0)
    predictedPrice = Column(Float, default=0)

    def __repr__(self):
        return f"<Item name={self.name} price={self.predictedPrice}>"
