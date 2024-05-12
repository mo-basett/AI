import streamlit as st
import pickle
import numpy as np
st.header("AI project")
st.subheader("Enter data")
col1, col2= st.columns(2)

with col1:
    Age = st.text_input("Age")
    Sex = st.selectbox("Sex",("M", "F"))
    ChestPainType = st.selectbox("ChestPainType",('ATA', 'NAP', 'ASY', 'TA'))
    RestingBP = st.text_input("RestingBP")
    Cholesterol = st.text_input("Cholesterol")
    FastingBS = st.text_input("FastingBS")

with col2:
    RestingECG = st.selectbox("RestingECG",('Normal', 'ST', 'LVH'))
    MaxHR = st.text_input("MaxHR")
    ExerciseAngina = st.selectbox("ExerciseAngina",("M", "F"))
    Oldpeak = st.text_input("Oldpeak")
    ST_Slope = st.selectbox("ST_Slope",('Up', 'Flat', 'Down'))



!wget https://github.com/mo-basett/AI/blob/c0b9eb68d118b27449ea9d501ebb76916f7d76f1/label.pkl?raw=true
!wget https://github.com/mo-basett/AI/blob/c0b9eb68d118b27449ea9d501ebb76916f7d76f1/DT.pkl?raw=true
if st.button("Predict"):
    # Load the model
    with open("DT.pkl?raw=true", "rb") as f:
        D_xxx = pickle.load(f)
    # Load the label encoder
    with open("label.pkl?raw=true", "rb") as f:
        label_encoder = pickle.load(f)
    
    # Encode categorical variables
    Sex_encoded = label_encoder.fit_transform([Sex])[0]
    ChestPainType_encoded = label_encoder.fit_transform([ChestPainType])[0]
    RestingECG_encoded = label_encoder.fit_transform([RestingECG])[0]
    ExerciseAngina_encoded = label_encoder.fit_transform([ExerciseAngina])[0]
    ST_Slope_encoded = label_encoder.fit_transform([ST_Slope])[0]
    
    # Create a list of input values
    numbers = [Age, Sex_encoded, ChestPainType_encoded, Cholesterol, FastingBS,
               RestingECG_encoded, MaxHR, ExerciseAngina_encoded, Oldpeak, ST_Slope_encoded]
    
    # Convert numeric inputs to float
    
    # Make prediction
    calclogin = D_xxx.predict([numbers])
    
    # Display prediction
    if calclogin == 1:
        st.write('Prediction: M')
    else:
        st.write('Prediction: B')
