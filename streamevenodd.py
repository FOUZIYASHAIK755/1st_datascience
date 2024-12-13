import streamlit as st
st.title("this is my first streamlit application")
st.title("let's find even or odd numbers")
a=st.number_input("enter the number",min_value=1,step=1)
if st.button("even/odd"):
    if a%2==0:
        st.success(f"{a} is a even number")
    else:
        st.error(f"{a} is an odd number")
