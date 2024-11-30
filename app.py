import streamlit as st
import pandas as pd
from data_intake.data_intake import get_data

# Initial message to indicate the app is running
st.write("Streamlit app is running")

# Create an input widget for the user to specify the number of days
no_of_days = st.number_input(
    'Enter the number of days', 
    min_value=1,   # Minimum allowed value
    max_value=10,  # Maximum allowed value
    value=1        # Default value
)

# Call the `get_data` function from the custom `data_intake` module
# Pass the user-specified number of days as a parameter
data = get_data(no_of_days)

# Display the retrieved data in a scrollable and interactive table
# The `st.dataframe` function renders a DataFrame in Streamlit
st.dataframe(data)
