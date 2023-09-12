import streamlit as st
import pandas as pd

st.set_page_config(page_title='WFL')

with st.container():
    st.subheader('Seja muito bem vindo ao meu mundo!')
    st.title('Wellington Facciolla Lopes')
    st.image('https://www.instagram.com/p/BjkUMdpFiiN/')
    st.write('Conheça mais sobre mim: [Clique aqui](https://www.instagram.com/wfacciolla/)')
with st.container():
    st.write('---')
    st.write('Nascido no interior de São Paulo')
    selecione = st.selectbox("Selecione",['Cadastrar','Visualizar'])
    if selecione == 'Cadastrar':
        st.write('Cadastros')
    if selecione == 'Visualizar':
        st.write('Visualização')