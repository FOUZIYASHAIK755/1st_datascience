import streamlit as st
st.title("calculating gross salary of an employee")
salary =  st.number_input("Enter your salary", value=0)
hra=0
da=0
gs=0
if salary < 10000:
    hra = (67 / 100) * salary
    da = (73 / 100) * salary

elif salary >= 10000 and salary <= 20000:
    hra = (69 / 100) * salary
    da = (76 / 100) * salary

elif salary > 20000:
    hra = (73 / 100) * salary
    da = (89 / 100) * salary

gs = hra + da + salary
st.write(f"your gross salary:{gs}")
st.write(f"hra of your salary:{hra}")
st.write(f"da of your salary:{da}")