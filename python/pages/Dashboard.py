import streamlit as st

st.title("Dashboard")
st.subheader('Deatails:')

col1, col2 = st.columns(2)

with col1:
    if 'user_data' in st.session_state:
        user = st.session_state['user_data']
        st.write("NAME    :", user['name'])
        st.write("EMAIL   :", user['email'])
        st.write("PASSWORD: ********")
    else:
        st.warning("No user data found. Please submit the form on the main page.")

with col2:
    st.image(r'python/images/code.png')


st.write("""THIS WEBSITE IS FOR KNOWNING ABOUT OUR
            SOLAR SYSTEM AND PLANETS SO PLEASE INJOY 
            THIS WEBSITE AND READ FOR KNOWLEDGE HAVE
            A BEST EXPERIENCE""")

st.divider()
st.text('click here to visit my youtube channel:')
st.markdown("https://www.youtube.com/channel/UCuDpJGQky9Bgj2z_ugS8GfA")
st.image(r'python/images/youtube.jpg')
st.divider()
st.text('click here to visit my instagram:')
st.markdown('https://www.instagram.com/saketh_437?igsh=ODRqbjYwenkyN2F3')
st.image('python/images/instagram.jpg')
st.divider()
st.write('PLEASE SUPPORT ME ON YOUTUBE AND INSTAGRAM')
st.write('IF YOU WANT YOU CONTACT ME YOU CAN MESSAGE ON INSTAGRAM')

dol1, dol2, dol3 = st.columns(3)
with dol1:
    st.write('')
with dol2:
    st.write('--:THANK YOU:--')
with dol3:
    st.write('')
