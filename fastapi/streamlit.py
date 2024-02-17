# streamlit_app/app.py
import streamlit as st
import requests

st.title("Iris Flower Classification")

# User input form
sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.4, 0.1)
sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.5, 0.1)
petal_length = st.slider("Petal Length", 1.0, 7.0, 1.3, 0.1)
petal_width = st.slider("Petal Width", 0.1, 2.5, 0.2, 0.1)

user_input = {
    "sepal_length": sepal_length,
    "sepal_width": sepal_width,
    "petal_length": petal_length,
    "petal_width": petal_width,
}

response = None
if st.button("Run"):
    # Make prediction API request
    response = requests.post("http://127.0.0.1:8000/predict", json=user_input)

    if response.status_code == 200:
        result = response.json()
        st.subheader("Prediction Result:")
        st.write(f"Predicted Class: {result['class_name']}")
    else:
        st.subheader("Error:")
        st.write("Failed to make a prediction. Please check your inputs.")
