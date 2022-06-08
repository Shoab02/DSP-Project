import pandas as pd
from sqlalchemy.orm import Session
import db_models


def create_cars_predictions_with_dataframe(
    db: Session,
    cars_predictions_df: pd.DataFrame
):
    row_index = int(get_last_index(db))+1
    cars = []

    end_col = cars_predictions_df.shape[0]
    if cars_predictions_df.shape[0] ==1:
        end_col = 2


    for i in range(0,end_col-1):
        cars.append(db_models.Car(
            id=row_index,
            powerPS=int(cars_predictions_df.iloc[i]['powerPS']),
            vehicleType=cars_predictions_df.iloc[i]['vehicleType'],
            brand=cars_predictions_df.iloc[i]['brand'],
            fuelType=cars_predictions_df.iloc[i]['fuelType'],
            kilometer=float(cars_predictions_df.iloc[i]['kilometer']),
            predictedPrice=float(cars_predictions_df.iloc[i]['predictedPrice'])
        )
        
        )
        row_index=row_index+1
        

    db.bulk_save_objects(cars)
    db.commit()
    
    return cars_predictions_df


def get_car_predictions(db: Session):
    return db.query(db_models.Car).all()

def get_last_index(db: Session):
    index_ob = db.query(db_models.Car.id).order_by(db_models.Car.id.desc()).first()
    return index_ob['id']
