from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class Car(BaseModel):
    dateCrawled:str
    name:str
    seller:str
    offerType:str
    abtest:str
    vehicleType:str
    yearOfRegistration:int
    gearbox:str
    powerPS:int
    model:str
    kilometer:float
    monthOfRegistration:int
    fuelType:str
    brand:str
    notRepairedDamage:str
    dateCreated:str
    nrOfPictures:int
    postalCode:float
    lastSeen:str