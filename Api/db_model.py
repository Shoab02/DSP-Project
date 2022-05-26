from db import Base
from sqlalchemy import String,Boolean,Integer,Float,Column,Date

class Car(Base):
    __tablename__ = 'car_predictions'
    id=Column(Integer,primary_key=True)
    dateCrawled=Column(String)
    name=Column(String)
    seller=Column(String)
    offerType=Column(String)
    abtest=Column(String)
    vehicleType=Column(String(255))
    yearOfRegistration=Column(String,default=0)
    gearbox=Column(String)
    powerPS=Column(Integer,default=0)
    model=Column(String)
    kilometer=Column(Float,default=0)
    monthOfRegistration=Column(Integer,default=0)
    fuelType=Column(String(255))
    brand=Column(String(255))
    notRepairedDamage=Column(String)
    dateCreated=Column(String)
    nrOfPictures=Column(Integer,default=0)
    postalCode=Column(Float,default=0)
    lastSeen=Column(String)
    price=Column(Float,default=0)
        
    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"