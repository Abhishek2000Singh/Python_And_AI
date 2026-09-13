import streamlit as st
import pandas as pd
import numpy as np

## Title of Application
st.title("My First Streamlit App")

##Display a Simple Text
st.write("Hello, welcome to my first Streamlit app! This is a simple example to demonstrate the capabilities of Streamlit.")

## Display a DataFrame
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4, 5],
    'Column 2': ['A', 'B', 'C', 'D', 'E']
})

st.write("Here's a simple DataFrame:")
##st.dataframe(df)
st.write(df)

## Line Chart Example
chart_data = pd.DataFrame(
    np.random.randn(20, 4),
    columns=['A', 'B', 'C','D']
)
st.line_chart(chart_data)