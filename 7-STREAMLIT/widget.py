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


data ={
    "Name":["John","Jane","Jake","Jill"],
    "Age":[23,23,25,30],
    "City":["Kolkata","Delhi","Gurugram","Pune"]
}
df = pd.DataFrame(data)
df.to_csv("Sample.csv")
st.write(df)

upload_file = st.file_uploader("choose your csv or txt",type="csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)

