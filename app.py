import streamlit as st
import joblib

# Load the trained model
model = joblib.load("model.pkl")

# Page title
st.title("Smart Helpdesk Ticket Classifier")

# Input box
ticket = st.text_area("Enter your IT support ticket:")

# Predict button
if st.button("Classify Ticket"):
    if ticket.strip():
        prediction = model.predict([ticket])[0]
        st.success(f"Predicted Category: {prediction}")
    else:
        st.warning("Please enter a ticket description.")