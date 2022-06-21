import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from request import tempPostRequest, postJsonRequest


def upload_file():
    selected_file_display = st.empty()
    selected_file = selected_file_display.file_uploader(
        label="Upload your csv file", type=["csv"])
    return selected_file


def user_input():
    data = []
    powerPS = st.number_input("PowerPS")
    data.append(powerPS)
    vehicleType = st.selectbox(
        "VehicleType",
        (
            'limousine', 'kombi', 'kleinwagen',
            'cabrio', 'bus', 'coupe', 'suv', 'any'
        )
    )
    data.append(vehicleType)
    brand = st.selectbox(
        "Brand",
        (
            'bmw', 'ford', 'volkswagen', 'renault', 'audi', 'opel',
            'mercedes_benz', 'fiat', 'suzuki', 'toyota', 'kia', 'mitsubishi',
            'peugeot', 'alfa_romeo', 'mazda', 'citroen', 'sonstige_autos',
            'seat', 'nissan', 'mini', 'skoda', 'daewoo', 'honda', 'subaru',
            'smart', 'volvo'
        )
    )
    data.append(brand)
    fuelType = st.selectbox("Fuel_Type", ("Petrol", "Diesel", "benzin"))
    data.append(fuelType)
    kilometer = st.number_input("Kms_Driven")
    data.append(kilometer)
    return data


def main():
    st.title("Loading data option")
    selected = option_menu(
        None,
        ["Upload_file", 'Input_data'],
        default_index=0,
        orientation="horizontal", menu_icon="app-indicator",
        styles={
            "container": {
                "padding": "5!important", "background-color": "#fafafa"
            },
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {
                "font-size": "16px", "text-align": "left", "margin": "0px",
                "--hover-color": "#eee"
            },
            "nav-link-selected": {"background-color": "#02ab21"},
        }
    )

    alert_message = st.sidebar.empty()  # keep space
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
        output = user_input()
        result = 0
        if predict_button:
            result = postJsonRequest(output)
            st.success(
                'The prediction of car price is {}'.format(result[0][-1]))


if __name__ == '__main__':
    main()
