import streamlit as st
import pandas

st.set_page_config(layout='wide')

with open('about_me.txt') as file:
    content = file.read()

st.markdown("""
<style>
h1 {
    color: pink;
    font: monaco
    font-size: 36px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


col1, col2 = st.columns([1, 3])
col3 = st.container()
col4, col5 = st.columns(2)

with col1:
    st.image('images/Dami_image.png', width=400, use_column_width='auto', output_format='auto')

with col2:
    st.title('Dami Fajinmi')
    st.info(content)


with col3:
    text = """ 
    <h1> Below you can find some Python Apps that I have built </h1>
    """
    st.write(text, unsafe_allow_html=True)

df = pandas.read_csv('data.csv', sep=';')


with col4:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col5:
    for index, row in df[10:].iterrows():
        st.header(row['title'])