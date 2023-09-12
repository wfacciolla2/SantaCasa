import streamlit as st
import Pages.Cliente.Cadastro as Cadastro_cliente
def main():
    def login():
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        if st.button("Login"):
            if username == "santacasa" and password == "123":
                st.success("Login realizado com sucesso!")
                st.session_state['logged_in'] = True
                # Redirecionar para a página restrita
                restricted_page()
            else:
                st.error("Usuário ou senha inválidos")

    st.title("Cadastro: ")
    # Verifica se o usuário está logado
    if not is_user_logged_in():
        st.warning("Você não está logado. Faça o login primeiro!")
        login()
    else:
        # Página restrita acessível apenas para usuários logados
        st.success(f"Bem-vindo(a)!")

        # Adicione o conteúdo da página restrita aqui

        logout_button()
def is_user_logged_in():
    # Lógica para verificar se o usuário está logado
    # Retorne True se o usuário estiver logado e False caso contrário
    # Você pode usar cookies, sessões ou qualquer outro método de autenticação aqui
    return st.session_state.get('logged_in', False) # Exemplo: sempre retorna True para fins de demonstração

def restricted_page():
    # Conteúdo da página restrita
    st.info("Conectado com sucesso!")
    return Cadastro_cliente.save_name(
        nome= st.text_input("nome:"),
        nome_mae= st.text_input("Nome da mae:"),
        numero_cartao= st.text_input("Cartão SUS:"),
        cpf= st.text_input("CPF:"),
        rg= st.text_input("RG"),
        data_nascimento= st.text_input("Nascimento:"),
        sexo= st.selectbox('Sexo', ['Masculino', 'Feminino']),
        telefone= st.text_input("Telefone:"),
        endereco= st.text_input("Endereço: "),
        cep= st.text_input("CEP:"),
        municipio= st.text_input("Municipio:"),
        estado= st.text_input("Estado:"),
        atendente= st.text_input("Atendente")


    )

def logout_button():
    if st.button("Sair"):
        st.session_state['logged_in'] = False
        st.info("Você saiu com sucesso!")
if __name__ == "__main__":
    main()