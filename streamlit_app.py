import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('Insurance_linear_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the input features
input_features = ['age', 'gender', 'bmi', 'bloodpressure', 'diabetic', 'children', 'smoker', 'region']

# Create a Streamlit app
st.header("Insurance Premium Prediction")
st.subheader("Enter your details to predict your insurance claim amount")

# Input fields for user data
age = st.number_input("Age", min_value=0, max_value=120, value=25)
gender = st.selectbox("Gender", options=["male", "female"])
bmi = st.number_input("BMI", min_value=0.0, max_value=50.0, value=25.0)
bloodpressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=120)
diabetic = st.selectbox("Diabetic", options=["Yes", "No"])
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", options=["Yes", "No"])
region = st.selectbox("Region", options=["southeast", "southwest", "northeast", "northwest"])

# Create a button to submit the input
submit_button = st.button("Predict Claim Amount")

# If the submit button is clicked
if submit_button:
    # Create a dictionary to store the user input
    user_input_dict = {
        'age': age,
        'gender': 1 if gender == "male" else 0,
        'bmi': bmi,
        'bloodpressure': bloodpressure,
        'diabetic': 1 if diabetic == "Yes" else 0,
        'children': children,
        'smoker': 1 if smoker == "Yes" else 0,
        'region': 2 if region == "southeast" else (3 if region == "southwest" else (4 if region == "northeast" else 1))
    }

    # Convert the user input to a numpy array
    user_input_array = np.array(list(user_input_dict.values())).reshape(1, -1)

    # Use the model to predict the claim amount
    claim_amount = model.predict(user_input_array)[0]

    # Display the predicted claim amount
    st.success(f"Predicted Claim Amount: {claim_amount:.2f}")
