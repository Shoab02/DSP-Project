from pydantic import BaseModel
import datetime


class Car(BaseModel):
    id: int
    pred_time: datetime.datetime
    powerPS: int
    vehicleType: str
    brand: str
    fuelType: str
    kilometer: float
    predictedPrice: float

    class Config:
        orm_mode = True
