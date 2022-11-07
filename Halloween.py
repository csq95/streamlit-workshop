import streamlit as st
import numpy as np
st.title("Happy Weekend!")

st.write(
    "Let's try a to find the largest number!"
)
num1 = st.number_input("Enter first number = ")
num2 = st.number_input("Enter second number = ")
num3 = st.number_input("Enter third number = ")

if (num1>=num2) and (num1>=num3) :
    st.write(num1,"is the largest.")
elif (num2>=num1) and (num2>=num3) :
    st.write(num2,"is the largest.")
else :
    st.write(num3,"is the largest.")
