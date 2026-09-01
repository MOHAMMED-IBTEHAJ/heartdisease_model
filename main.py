import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("model.pkl")
st.title("Heart Diabetes Prediction App")
st.write("This app predicts the likelihood of heart disease and diabetes based on user input.")
age = st.number_input("Age", min_value=0, max_value=120, value=50)
current_smoker = st.selectbox("Current Smoker", [1, 0])
cigsperday = st.number_input("Cigarettes per Day", min_value=0,max_value=100, value=0)
bpmeds = st.selectbox("On Blood Pressure Medication", [1, 0])
prevalent_stroke = st.selectbox("History of Stroke", [1, 0])
daiabetes = st.selectbox("History of Diabetes", [1, 0])
totchol = st.number_input("Total Cholesterol (mg/dL)", min_value=0, max_value=1000, value=200)  
sysbp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=0, max_value=300, value=120)
diabp = st.number_input("Diastolic Blood Pressure (mmHg)", min_value=0, max_value=200, value=80)
bmi = st.number_input("Body Mass Index (BMI)", min_value=0.0, max_value=100.0, value=25.0)  
heart_rate = st.number_input("Heart Rate (bpm)", min_value=0, max_value=300, value=70)
glucose = st.number_input("Glucose Level (mg/dL)", min_value=0, max_value=1000, value=90)

if st.button("Predict"):
    input_data = np.array([[age, current_smoker, cigsperday, bpmeds, prevalent_stroke, daiabetes, totchol, sysbp, diabp, bmi, heart_rate, glucose]])
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("The model predicts that you are at risk of heart disease and diabetes.")
    else:
        st.success("The model predicts that you are not at risk of heart disease and diabetes.")