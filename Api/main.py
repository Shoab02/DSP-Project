import uvicorn
import pandas as pd
from used_cars.inference import make_predictions
from fastapi import FastAPI, Depends, UploadFile
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from pydantic import BaseModel


from database import SessionLocal, engine
import db_models
import crud

load_dotenv('./.env')
db_models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Car Price Prediction',
    version='1.0',
    description=''
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Used to test endpoint singlepredict


class Car(BaseModel):
    powerPS: str
    vehicleType: str
    brand: str
    fuelType: str
    kilometer: str

    class Config:
        orm_mode = True


@app.get('/')
@app.get('/home')
def read_home():
    return {'message': 'Thank you for using our car price prediction app'}

# When the feature values are received through a file uploaded by the user,


@app.post("/predict")
def predict(csv_file: UploadFile, db: Session = Depends(get_db)):
    user_data_df = pd.read_csv(csv_file.file, encoding='latin-1')

    predictions = make_predictions(user_data_df)
    user_data_df = user_data_df.fillna("")
    predictions = [round(prediction) for prediction in predictions]
    f_df = user_data_df.join(pd.DataFrame(
        predictions, columns=['predictedPrice']))

    crud.create_cars_predictions_with_dataframe(db, f_df)

    return {"status": 200,
            "message": "Successful",
            "results": f_df.values.tolist()}


# When the feature values are received as single values

@app.post("/predictSingle")
def predict_signle(req: Car, db: Session = Depends(get_db)):
    car_dict = {
        "powerPS": float(req.powerPS),
        "vehicleType": req.vehicleType,
        "brand": req.brand,
        "fuelType": req.fuelType,
        "kilometer": float(req.kilometer)
    }

    single_df = pd.DataFrame(car_dict, index=[0])

    predictions = make_predictions(single_df)
    single_df = single_df.fillna("")
    f_df = single_df.join(
        pd.DataFrame(
            [round(predictions[0])],
            columns=['predictedPrice']
        )
    )

    crud.create_cars_predictions_single(db, f_df)

    return {"status": 200,
            "message": "Successful",
            "results": f_df.values.tolist()}
            


# To retrieve all the stored predictions
@app.get('/car_predictions', status_code=200)
def get_all_preds(db: Session = Depends(get_db)):
    cars = crud.get_car_predictions(db)

    return {"status": 200,
            "message": "Successful",
            "results": cars}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
