import uvicorn
import pandas as pd
from used_cars.inference import make_predictions
from fastapi import FastAPI, Depends, UploadFile
from sqlalchemy.orm import Session
from dotenv import load_dotenv

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
    f_df = user_data_df.join(pd.DataFrame(
        predictions, columns=['predictedPrice']))

    crud.create_cars_predictions_with_dataframe(db, f_df)

    return {"status": 200,
            "message": "Successful",
            "results": f_df.values.tolist()}


# When the feature values are received as single values

# @app.post("/predictSingle")
# def predict(req:Car):

#    id= np.random.randint(100000)
#    dateCrawled=req.dateCrawled,
#    name=req.name,
#    offerType=req.offerType,
#    abtest=req.abtest,
#    vehicleType=req.vehicleType,
#    yearOfRegistration=req.yearOfRegistration,
#    gearbox=req.gearbox,
#    powerPS=req.powerPS,
#    model=req.model,
#    kilometer=req.kilometer,
#    monthOfRegistration=req.monthOfRegistration,
#    fuelType=req.fuelType,
#    brand=req.brand,
#    notRepairedDamage=req.notRepairedDamage,
#    dateCreated=req.dateCreated,
#    nrOfPictures=req.nrOfPictures,
#    postalCode=req.postalCode,
#    lastSeen=req.lastSeen

#        values = list([id,dateCrawled,name,seller,offerType,abtest,vehicleType,yearOfRegistration,gearbox,powerPS,model,kilometer,monthOfRegistration,fuelType,brand,notRepairedDamage,dateCreated,nrOfPictures,postalCode,lastSeen
# ])
#    )

#    predictions = make_predictions(user_data_df)
#    user_data_df = user_data_df.fillna("")
#    f_df = user_data_df.join(pd.DataFrame([predictions[0]],columns=['Price']))

#    return f_df.values.tolist()


# To retrieve all the stored predictions
@app.get('/car_predictions', status_code=200)
def get_all_preds(db: Session = Depends(get_db)):
    cars = crud.get_car_predictions(db)

    return {"status": 200,
            "message": "Successful",
            "results": cars}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
