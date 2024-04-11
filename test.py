import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os


encoded_data = [
    # Home Ownership: MORTGAGE, OTHER, OWN, RENT
    1, 0, 0, 0,
    # Loan Intent: DEBTCONSOLIDATION, EDUCATION, HOMEIMPROVEMENT, MEDICAL, PERSONAL, VENTURE
    1, 0, 0, 0, 0, 0,
    # Loan Grade: A, B, C, D, E, F, G
    1, 0, 0, 0, 0, 0, 0,
    # Default History: N, Y
    1, 0,
    # Age Group: 20-25, 26-35, 36-45, 46-55, 56-65
    1, 0, 0, 0, 0,
    # Income Group: high, high-middle, low, low-middle, middle
    0, 0, 0, 0, 1,
    # Loan Amount Group: large, medium, small, very large
    0, 1, 0, 0,
    # Numerical values
    4.0, 11.011695, 0.21, 3.0
]


model_path = 'best_model.pkl'
if os.path.exists(model_path):
    model = joblib.load(model_path)

model.predict(encoded_data)

