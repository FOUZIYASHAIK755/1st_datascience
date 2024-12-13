import streamlit as st
st.title("calculating the grades of students")
pro = st.number_input('enter project marks ')
inte = st.number_input('enter internal marks ')
ext = st.number_input('enter external marks ')
if (pro > 50 and inte > 50 and ext > 50):
    total = ((70 / 100) * pro + (10 / 100) * inte + (20 / 100) * ext)
    st.write(f'total:{total}')
    if total > 90:
        st.write('A grade')
    elif total > 80:
        st.write_stream('B grade')
    else:
        st.write('C grade')
else:
    if pro < 50:
        st.write('failed in project')
    if inte < 50:
        st.write('failed in internal')
    if ext < 50:
        st.write('failed in external')