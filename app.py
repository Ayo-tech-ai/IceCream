import streamlit as st
import pickle

# Load the pre-trained model
with open('lm_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set up the Streamlit interface
st.title("Profit Prediction App")
st.write("This app uses a machine learning model to make Profit predictions for Ice cream Sold.")

# Example input fields for the model
# Adjust the inputs based on your model's requirements
input = st.number_input("Enter value for input 1", min_value=25, max_value=120, step=1)


# Run prediction when button is clicked
if st.button("Predict"):
    # Prepare input data for prediction
    # Convert inputs into a format the model expects, e.g., a 2D array
    input_data = [[input]]
    prediction = model.predict(input_data)
    
    # Display prediction result
    st.write("Profit:", prediction[0])
