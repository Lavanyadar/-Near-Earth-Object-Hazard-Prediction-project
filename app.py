import streamlit as st
import pickle
import pandas as pd

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(
    page_title="NEO Hazard Prediction",
    page_icon="☄️",
    layout="centered"
)

st.title("☄️ Near Earth Object Hazard Prediction")

st.write("Enter asteroid details below:")

# Inputs
estimated_diameter_min = st.number_input(
    "Estimated Diameter Min (km)",
    min_value=0.0,
    value=0.1
)

estimated_diameter_max = st.number_input(
    "Estimated Diameter Max (km)",
    min_value=0.0,
    value=0.2
)

relative_velocity = st.number_input(
    "Relative Velocity (km/h)",
    min_value=0.0,
    value=50000.0
)

miss_distance = st.number_input(
    "Miss Distance (km)",
    min_value=0.0,
    value=1000000.0
)

absolute_magnitude = st.number_input(
    "Absolute Magnitude",
    min_value=0.0,
    value=22.0
)

if st.button("Predict"):

    input_data = pd.DataFrame({
    "est_diameter_min": [estimated_diameter_min],
    "est_diameter_max": [estimated_diameter_max],
    "relative_velocity": [relative_velocity],
    "miss_distance": [miss_distance],
    "absolute_magnitude": [absolute_magnitude]
})

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Hazardous Asteroid")
    else:
        st.success("✅ Non-Hazardous Asteroid")