import streamlit as st
import pandas as pd
import numpy as np
import json
import csv
from streamlit_option_menu import option_menu
from request import getDisplayHistory


def main():
    html_temp = """
                   <div style="background-color:green;padding:10px">
                   <h3 style="color:white;text-align:center;"> Car Price prediction history </h3>
                   </div>
                   """
    st.markdown(html_temp, unsafe_allow_html=True)

    history = getDisplayHistory()
    #st.write(history)
    data = history['results']
    df = pd.DataFrame(data)
    display = df.reindex(columns=['id','powerPS','brand','vehicleType','fuelType','kilometer','predictedPrice'])
    st.table(display)
if __name__ == '__main__':
    main()
