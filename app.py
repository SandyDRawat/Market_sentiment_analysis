import streamlit as st
import pandas as pd
from data_intake.data_intake import get_data


st.write("Streamlit app is running")


no_of_days = st.number_input('Enter the number of days', min_value=1, max_value=10, value=1)

data = get_data(no_of_days)

#st.write(data)
st.dataframe(data)


