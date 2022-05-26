from http import HTTPStatus
from telnetlib import STATUS
import joblib
import json
import uvicorn
import pandas as pd
import numpy as np
import db_model
from pydantic import BaseModel
from used_cars.inference import make_predictions
from fastapi import FastAPI, File, UploadFile, status
from typing import Optional,List
from Car import Car
import db

app = FastAPI(title='Car Price Prediction', version='1.0',
              description='')

db = db.SessionLocal()

@app.get('/')
@app.get('/home')
def read_home():
    return {'message': 'Thank you for using our car price prediction app'}

# When the feature values are received through a file

@app.post("/predict")
def predict(csv_file:UploadFile):
    user_data_df = pd.read_csv(csv_file.file,encoding='latin-1')
    
    predictions = make_predictions(user_data_df)
    user_data_df = user_data_df.fillna("")
    f_df = user_data_df.join(pd.DataFrame(predictions,columns=['Price']))
    
    add_to_db(f_df)

    return {"status":200,
            "message":"Successful",
            "results":f_df.values.tolist()}


def add_to_db(f_df):

    for i in range(0,f_df.shape[0]-1):
            new_car=db_model.Car(
            id=i,
            dateCrawled=f_df.iloc[i]['dateCrawled'],
            name=f_df.iloc[i]['name'],
            seller=f_df.iloc[i]['seller'],
            offerType=f_df.iloc[i]['offerType'],
            abtest=f_df.iloc[i]['abtest'],
            vehicleType=f_df.iloc[i]['vehicleType'],
            yearOfRegistration=int(f_df.iloc[i]['yearOfRegistration']),
            gearbox=f_df.iloc[i]['gearbox'],
            powerPS=int(f_df.iloc[i]['powerPS']),
            model=f_df.iloc[i]['model'],
            kilometer=float(f_df.iloc[i]['kilometer']),
            monthOfRegistration=int(f_df.iloc[i]['monthOfRegistration']),
            fuelType=f_df.iloc[i]['fuelType'],
            brand=f_df.iloc[i]['brand'],
            notRepairedDamage=f_df.iloc[i]['notRepairedDamage'],
            dateCreated=f_df.iloc[i]['dateCreated'],
            nrOfPictures=int(f_df.iloc[i]['nrOfPictures']),
            postalCode=float(f_df.iloc[i]['postalCode']),
            lastSeen=f_df.iloc[i]['lastSeen'],
            price=float(f_df.iloc[i]['price'])
            )

            db.add(new_car)
            db.commit()

    

# When the feature values are received as single values

#@app.post("/predictSingle")
#def predict(req:Car):

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
#])
#    )

#    predictions = make_predictions(user_data_df)
#    user_data_df = user_data_df.fillna("")
#    f_df = user_data_df.join(pd.DataFrame([predictions[0]],columns=['Price']))
    
#    return f_df.values.tolist()

#To retrieve all the stored predictions

@app.get('/predHistory',status_code=200)
def get_all_preds():
    cars = db.query(db_model.Car).all()

    return {"status":200,
            "message":"Successful",
            "results":cars}
    
if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)