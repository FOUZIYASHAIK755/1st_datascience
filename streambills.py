import  streamlit as st
st.title("finding the shopping bills percentage in salary")
sal=st.number_input("salary amount:",min_value=1)
fbill=st.number_input("first shopping bill:",min_value=1)
sbill=st.number_input("second shopping bill: ",min_value=1)
tbill=st.number_input("third shopping bill:",min_value=1)
shoppingbill= fbill + sbill +tbill
st.success(f"total shopping bill {shoppingbill}")
per=(shoppingbill/sal)*100
st.success(f'total amount spend:{per}%')