import streamlit as st
import pandas as pd
import numpy as np

global df

def car_price_predictor():
    array = pd.DataFrame(np.random.randn(10, 5), columns=('col %d' % i for i in range(5)))
    return array

def upload_file():

    # title of the app
    try:
        st.write(df)
    except Exception as e:
        print(e)
        st.write("Please upload file to the application")

def main():

    #df : pd.DataFrame = None
    #madePredictions = False

    #SIDE BAR
    # add a sidebar
    st.sidebar.subheader("Setting")
    # setup file upload
    selected_file = st.sidebar.file_uploader(label="Upload your csv or Excel file",type=["csv", "xlsx"])
    alert_message = st.sidebar.empty()

    predict_button = st.sidebar.button(label="Predict", key="predict_button", on_click=car_price_predictor)

    #MAIN PAGE
    st.title("Car Price Prediction")
    selected_file_display = st.empty()

    if selected_file is not None:
        if not predict_button:
            print('the file is uploaded!')
            try:
                df = pd.read_csv(selected_file)
                selected_file_display.write(df)
            except Exception as e:
                print(e)
                df = pd.read_excel(selected_file)
                selected_file_display.write(df)
    else:
        selected_file_display.write("Please upload file to the application")

    prediction_table = st.empty()

    if predict_button and selected_file is not None:
        selected_file_display.empty()
        _array = car_price_predictor()
        prediction_table.table(_array)
    if predict_button and selected_file is None:
        alert_message.warning('Please upload the file first')

if __name__ == '__main__':
    main()
