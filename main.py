import streamlit as st
import pandas as pd


def salvar_dados(nome, nome_mae, numero_cartao, cpf, rg, data_nascimento, sexo, telefone, endereco, cep, municipio, estado, atendente):
    dados = {
        'Nome': [nome],
        'Nome da Mãe': [nome_mae],
        'Número do Cartão': [numero_cartao],
        'CPF': [cpf],
        'RG': [rg],
        'Data de Nascimento': [data_nascimento],
        'Sexo': [sexo],
        'Telefone': [telefone],
        'Endereço': [endereco],
        'CEP': [cep],
        'Município': [municipio],
        'Estado': [estado],
        'Atendente': [atendente]
    }
    df = pd.DataFrame(dados)
    # Verifica se o arquivo CSV já existe
    try:
        arquivo_csv = pd.read_csv('cadastro.csv')
        df = pd.concat([arquivo_csv, df], ignore_index=True)
    except FileNotFoundError:
        pass
    df.to_csv('cadastro.csv', index=False)
    st.title('Cadastro')
    nome = st.text_input('Nome')
    nome_mae = st.text_input('Nome da Mãe')
    numero_cartao = st.text_input('Número do Cartão')
    cpf = st.text_input('CPF')
    rg = st.text_input('RG')
    data_nascimento = st.date_input('Data de Nascimento')
    sexo = st.selectbox('Sexo', ['Masculino', 'Feminino'])
    telefone = st.text_input('Telefone')
    endereco = st.text_input('Endereço')
    cep = st.text_input('CEP')
    municipio = st.text_input('Município')
    estado = st.text_input('Estado')
    atendente = st.text_input('Nome do Atendente')

    if st.button('Salvar'):
        salvar_dados(nome, nome_mae, numero_cartao, cpf, rg, data_nascimento, sexo, telefone, endereco, cep, municipio, estado, atendente)
        st.success('Dados salvos com sucesso!')