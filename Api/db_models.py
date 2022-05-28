from database import Base
from sqlalchemy import (
    String,
    Integer,
    Float,
    Column,
)


class Car(Base):
    __tablename__ = 'car_predictions'
    id = Column(Integer, primary_key=True, index=True)
    powerPS = Column(Integer, default=0)
    vehicleType = Column(String(255))
    brand = Column(String(255))
    fuelType = Column(String(255))
    kilometer = Column(Float, default=0)
    predictedPrice = Column(Float, default=0)

    def __repr__(self):
        return f"<Item name={self.name} price={self.predictedPrice}>"
