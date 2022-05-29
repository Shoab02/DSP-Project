from request import tempPostRequest
import streamlit as st
import pandas as pd
import numpy as np
import json
import csv
from streamlit_option_menu import option_menu

def side_bar():

    st.sidebar.subheader("Setting")
    # setup file upload
    selected_file = st.sidebar.file_uploader(label="Upload your csv or Excel file", type=["csv", "xlsx"])


    alert_message = st.sidebar.empty()
    predict_button = st.sidebar.button(label="Predict", key="predict_button")

    return selected_file, alert_message, predict_button


def prediction():
    selected_file_display = st.empty()
    prediction_table = st.empty()
    selected_file, alert_message, predict_button = side_bar()
    if selected_file is not None:
        if not predict_button:
            print('the file is uploaded!')
            df = pd.read_csv(selected_file, encoding='latin-1')
            selected_file_display.write(df)

    else:
        selected_file_display.write("Please upload file to the application")

    if predict_button and selected_file is not None:
        result = tempPostRequest(selected_file)
        headers = list(pd.read_csv(selected_file, encoding='latin-1').columns.tolist())
        headers.append('Prediction price')
        data = result['results']
        display = pd.DataFrame(data, columns=headers)
        prediction_table.table(display)
    if predict_button and selected_file is None:
        alert_message.warning('Please upload the file first')

def main():
    st.title("Car Price Prediction")
    prediction()


if __name__ == '__main__':
    main()