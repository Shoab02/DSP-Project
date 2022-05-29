from request import tempPostRequest
import streamlit as st
import pandas as pd
import numpy as np
import json
import csv
from streamlit_option_menu import option_menu



def upload_file():
    selected_file_display = st.empty()
    selected_file = selected_file_display.file_uploader(label="Upload your csv file", type=["csv"])
    return selected_file

def user_input():

    data = []
    powerPS = st.number_input("PowerPS")
    data.append(powerPS)
    vehicleType = st.selectbox("VehicleType", ('limousine', 'kombi', 'kleinwagen', 'cabrio', 'bus', 'coupe',
                                               'suv', 'any'))
    data.append(vehicleType)
    brand = st.selectbox("Brand", ('bmw', 'ford', 'volkswagen', 'renault', 'audi', 'opel',
                                   'mercedes_benz', 'fiat', 'suzuki', 'toyota', 'kia', 'mitsubishi',
                                   'peugeot', 'alfa_romeo', 'mazda', 'citroen', 'sonstige_autos',
                                   'seat', 'nissan', 'mini', 'skoda', 'daewoo', 'honda', 'subaru',
                                   'smart', 'volvo'))
    data.append(brand)
    fuelType = st.selectbox("Fuel_Type", ("Petrol", "Diesel", "benzin"))
    data.append(fuelType)
    kilometer = st.number_input("Kms_Driven")
    data.append(kilometer)

    df = pd.DataFrame([data], columns=['powerPS', 'vehicleType', 'brand', 'fuelType', 'kilometer'])
    js = df.to_json()
    js = json.loads(js)
    return js


def main():
    html_temp = """
               <div style="background-color:green;padding:10px">
               <h5 style="color:white;text-align:center;">Streamlit Car Price Prediction  ML App </h5>
               </div>
               """
    st.markdown(html_temp, unsafe_allow_html=True)

    with st.sidebar:
         selected = option_menu(" Load data option", ["Upload_file", 'Input_data'],default_index=0)

    alert_message = st.sidebar.empty()
    predict_button = st.sidebar.button(label="Predict", key="predict_button")
    selected_file_display = st.empty()

    if selected == "Upload_file":
        selected_file = upload_file()
        if selected_file is not None:
            df = pd.read_csv(selected_file, encoding='latin-1')
            selected_file_display.write(df)

        if predict_button and selected_file is not None:
            result = tempPostRequest(selected_file)
            headers = list(df.columns)
            headers.append('Prediction price')
            data = result['results']
            display = pd.DataFrame(data, columns=headers)
            selected_file_display.table(display)
        if predict_button and selected_file is None:
            alert_message.warning('Please upload the file first')
    elif selected == "Input_data":
        Json = user_input()
        result = 0
        if predict_button:
             result = tempPostRequest(Json)
        st.success('The output is {} lacks'.format(result))

if __name__ == '__main__':
    main()
