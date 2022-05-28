from pydantic import BaseModel


class Car(BaseModel):
    id: int
    powerPS: int
    vehicleType: str
    brand: str
    fuelType: str
    kilometer: float
    predictedPrice: float

    class Config:
        orm_mode = True
