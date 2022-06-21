import streamlit as st
from PIL import Image


def main():
    html_temp = """
        <div style="background-color:green;padding:10px">
        <h2 style="color:white;text-align:center;">
            Welcome to Car Price Prediction  ML App
        </h2>
        </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    background = Image.open("7.jpg")
    col1, col2, col3 = st.columns([0.2, 5, 0.2])
    col2.image(background, use_column_width=True)


if __name__ == '__main__':
    main()
