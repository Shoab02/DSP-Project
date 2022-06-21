import pandas as pd
from sqlalchemy import desc
from sqlalchemy.orm import Session
import db_models


def create_cars_predictions_with_dataframe(
    db: Session,
    cars_predictions_df: pd.DataFrame
):

    cars = []

    for i in range(0, cars_predictions_df.shape[0]-1):
        cars.append(db_models.Car(
            powerPS=int(cars_predictions_df.iloc[i]['powerPS']),
            vehicleType=cars_predictions_df.iloc[i]['vehicleType'],
            brand=cars_predictions_df.iloc[i]['brand'],
            fuelType=cars_predictions_df.iloc[i]['fuelType'],
            kilometer=float(cars_predictions_df.iloc[i]['kilometer']),
            predictedPrice=float(cars_predictions_df.iloc[i]['predictedPrice'])
        )

        )

    db.bulk_save_objects(cars)
    db.commit()

    return cars_predictions_df


def create_cars_predictions_single(
    db: Session,
    cars_predictions_df: pd.DataFrame
):
    new_pred = db_models.Car(
        powerPS=int(cars_predictions_df['powerPS'][0]),
        vehicleType=cars_predictions_df['vehicleType'][0],
        brand=cars_predictions_df['brand'][0],
        fuelType=cars_predictions_df['fuelType'][0],
        kilometer=float(cars_predictions_df['kilometer'][0]),
        predictedPrice=float(cars_predictions_df['predictedPrice'][0])
    )
    db.add(new_pred)
    db.commit()

    return cars_predictions_df


def get_car_predictions(db: Session):
    return db.query(
        db_models.Car
    ).order_by(
        desc(db_models.Car.pred_time)
    ).all()
