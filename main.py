import streamlit as st

st.set_page_config(layout='wide')

with open('about_me.txt') as file:
    content = file.read()


col1, col2 = st.columns(2)

with col1:
    st.image('images/Dami_image.png', width=300)

with col2:
    st.title('Dami Fajinmi')
    st.info(content)



