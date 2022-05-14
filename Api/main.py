import joblib
import uvicorn
import numpy as np
import pandas as pd
from pydantic import BaseModel
from used_cars.inference import make_predictions
from fastapi import FastAPI, File, UploadFile
from fastapi import FastAPI

app = FastAPI(title='Car Price Prediction', version='1.0',
              description='')


@app.get('/')
@app.get('/home')
def read_home():
    return {'message': 'Thank you for using our car price prediction app'}

@app.post("/predict")
def predict(csv_file:UploadFile):
    user_data_df = pd.read_csv(csv_file.file,encoding='latin-1')
    predictions = make_predictions(user_data_df)

    #convertToDF(user_data_df,predictions.tolist())
    # # #return {'message':predictions.tolist()}
    return predictions.tolist()

    #return {'message':predictions[0]}

def convertToDF(user_data_df,predictions):
    #df= user_data_df.append(pd.DataFrame(predictions))
    df = pd.DataFrame(predictions)
    return df

    
if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)