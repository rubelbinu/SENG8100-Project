import streamlit as st
import joblib
import os
from tkinter import messagebox


def decode_data(encoded_data):
    # Decoding home ownership
    home_ownership = ["MORTGAGE", "OTHER", "OWN", "RENT"][encoded_data[:4].index(1)]
    # Decoding loan intent
    loan_intent = ["DEBTCONSOLIDATION", "EDUCATION", "HOMEIMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE"][encoded_data[4:10].index(1)]
    # Decoding loan grade
    loan_grade = ["A", "B", "C", "D", "E", "F", "G"][encoded_data[10:17].index(1)]
    # Decoding default history
    default_history = ["N", "Y"][encoded_data[17:19].index(1)]
    # Decoding age group
    age_group = ["20-25", "26-35", "36-45", "46-55", "56-65"][encoded_data[19:24].index(1)]
    # Decoding income group
    income_group = ["high", "high-middle", "low", "low-middle", "middle"][encoded_data[24:29].index(1)]
    # Decoding loan amount group
    loan_amount_group = ["large", "medium", "small", "very large"][encoded_data[29:33].index(1)]
    # Extracting numerical values
    numerical_values = {
        "Employment Length": encoded_data[33],
        "Loan Interest Rate": encoded_data[34],
        "Loan Percent Income": encoded_data[35],
        "Credit History": encoded_data[36]
    }

    return {
        "Home Ownership": home_ownership,
        "Loan Intent": loan_intent,
        "Loan Grade": loan_grade,
        "Default History": default_history,
        "Age Group": age_group,
        "Income Group": income_group,
        "Loan Amount Group": loan_amount_group,
        "Numerical Values": numerical_values
    }

model_path = 'best_model.pkl'
if os.path.exists(model_path):
    model = joblib.load(model_path)

st.title("Loan Approval Predictor")

# Dropdown for home ownership
home_ownership = st.selectbox("Home Ownership", ["MORTGAGE", "OTHER", "OWN", "RENT"])

# Dropdown for loan intent
loan_intent = st.selectbox("Loan Intent", ["DEBTCONSOLIDATION", "EDUCATION", "HOMEIMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE"])

# Dropdown for loan grade
loan_grade = st.selectbox("Loan Grade", ["A", "B", "C", "D", "E", "F", "G"])

# Dropdown for default history
default_history = st.selectbox("Default History", ["N", "Y"])

# Dropdown for age group
age_group = st.selectbox("Age Group", ["20-25", "26-35", "36-45", "46-55", "56-65"])

# Dropdown for income group
income_group = st.selectbox("Income Group", ["high", "high-middle", "low", "low-middle", "middle"])

# Dropdown for loan amount group
loan_amount_group = st.selectbox("Loan Amount Group", ["large", "medium", "small", "very large"])

# User input for employment length
employment_length = st.slider("Employment Length (years)", min_value=0, max_value=30, value=5)

# User input for loan interest rate
loan_interest_rate = st.slider("Loan Interest Rate (%)", min_value=0.0, max_value=20.0, value=8.0, step=0.1)

# User input for loan percent income
loan_percent_income = st.slider("Loan Percent Income (%)", min_value=0.0, max_value=100.0, value=20.0, step=0.1)

# User input for credit history
credit_history = st.slider("Credit History", min_value=0.0, max_value=1.0, value=0.75, step=0.01)

# Function to handle prediction
def predict_loan_approval():
    # Update encoded data with user input for categorical values
    encoded_data = [
        # Home Ownership: MORTGAGE, OTHER, OWN, RENT
        home_ownership == "MORTGAGE",
        home_ownership == "OTHER",
        home_ownership == "OWN",
        home_ownership == "RENT",
        # Loan Intent: DEBTCONSOLIDATION, EDUCATION, HOMEIMPROVEMENT, MEDICAL, PERSONAL, VENTURE
        loan_intent == "DEBTCONSOLIDATION",
        loan_intent == "EDUCATION",
        loan_intent == "HOMEIMPROVEMENT",
        loan_intent == "MEDICAL",
        loan_intent == "PERSONAL",
        loan_intent == "VENTURE",
        # Loan Grade: A, B, C, D, E, F, G
        loan_grade == "A",
        loan_grade == "B",
        loan_grade == "C",
        loan_grade == "D",
        loan_grade == "E",
        loan_grade == "F",
        loan_grade == "G",
        # Default History: N, Y
        default_history == "N",
        default_history == "Y",
        # Age Group: 20-25, 26-35, 36-45, 46-55, 56-65
        age_group == "20-25",
        age_group == "26-35",
        age_group == "36-45",
        age_group == "46-55",
        age_group == "56-65",
        # Income Group: high, high-middle, low, low-middle, middle
        income_group == "high",
        income_group == "high-middle",
        income_group == "low",
        income_group == "low-middle",
        income_group == "middle",
        # Loan Amount Group: large, medium, small, very large
        loan_amount_group == "large",
        loan_amount_group == "medium",
        loan_amount_group == "small",
        loan_amount_group == "very large",
        # Numerical values
        employment_length, 
        loan_interest_rate, 
        loan_percent_income, 
        credit_history
    ]
    # if 'model' in globals():
    #     prediction = model.predict([encoded_data])
    #     st.subheader("Prediction:")
    #     st.write(prediction)
    if 'model' in globals():
        prediction = model.predict([encoded_data])
        st.subheader("Prediction:")
        # Display prediction result
        if prediction[0] == 1:
            st.error("The loan application is predicted to be risky.")
        else:
            st.success("The loan application is predicted to be safe.")
    else:
        st.error("Model not found. Please ensure 'best_model.pkl' exists in the specified path.")

# Button to trigger prediction
if st.button("Predict"):
    predict_loan_approval()