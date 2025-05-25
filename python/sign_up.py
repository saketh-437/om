import streamlit as st
# tittle#
col1, col2, col3 = st.columns(3)
with col1:
    st.write('')
with col2:
    st.title('GALAXY')
with col3:
    st.write('')

st.sidebar.success('SETTINGS')

def Deatails():
    #name#
    x = st.text_input('name', key='name')
    # email#
    y = st.text_input('email', key='email')
    # password#
    p = st.text_input('password', type='password')
    #button#
    f = st.button('SUBMIT')
    if x and y and p:
        if f:
            st.session_state['user_data'] = {'name': x, 'email': y}
            st.success('THANKS FOR SUBMIT')
            st.text('NOW GO TO BROSWER')
            st.text('IF YOU WANT CHECK DEATAILS YOU CAN GO TO DASHBOARD')
    else:
        st.error('complete the form')
Deatails()
















