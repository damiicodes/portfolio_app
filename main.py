import streamlit as st
import pandas

st.set_page_config(layout='wide')

with open('about_me.txt') as file:
    content = file.read()

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url('https://images.unsplash.com/photo-1628029799784-50d803e64ea0?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=659&q=80');
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


add_bg_from_url()


col1, col2 = st.columns([1, 3])
col3 = st.container()
col4, empty_col, col5 = st.columns([1.5, 0.5, 1.5])


with col1:
    st.image('images/Dami_image.png', width=400, use_column_width='auto', output_format='auto')

with col2:
    st.title('Dami Fajinmi')
    st.write(f'<p> {content} </p>', unsafe_allow_html=True)


with col3:
    text = """ 
    <h1> Below you can find some Python Apps that I have built </h1>
    """
    st.write(text, unsafe_allow_html=True)

df = pandas.read_csv('data.csv', sep=';')


with col4:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Source Code]({row["url"]})')


with col5:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Source Code]({row["url"]})')