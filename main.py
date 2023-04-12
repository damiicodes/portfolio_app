import streamlit as st

st.set_page_config(layout='wide')

with open('about_me.txt') as file:
    content = file.read()


col1, col2 = st.columns([1, 3])
col3 = st.container()

with col1:
    st.image('images/Dami_image.png', width=400, use_column_width='auto', output_format='auto')

with col2:
    st.title('Dami Fajinmi')
    st.info(content)


with col3:
    text = """ 
    Below you can find some Python Apps I have built
    """
    st.write(text)