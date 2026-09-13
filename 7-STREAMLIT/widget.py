import streamlit as st
import pandas as pd

st.title("Streamlit Text Input Example")

name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 0, 100, 25)


if name:
    st.write(f"Hello, {name}! You are {age} years old.")
else:
    st.write("Please enter your name above.")

options = ["Python","Java","C++","JavaScript","Go","Ruby"]
choice = st.selectbox("Choose Your Fav Language: ",options)
st.write(f"Your selected option is:- {choice}")

