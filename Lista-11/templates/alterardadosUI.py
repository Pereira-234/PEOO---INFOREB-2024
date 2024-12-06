import streamlit as st
from views import View

class AlterarDadosUI:
    def main():
        st.header("Alterar Meus Dados")
        cliente_id = st.session_state["cliente_id"]
        cliente = View.cliente_listar_id(cliente_id)

        if cliente.nome == "admin":
            nova_senha = st.text_input("Nova senha", type="password")
            if st.button("Atualizar"):
                View.cliente_atualizar(cliente.id, cliente.nome, cliente.email, cliente.fone, nova_senha)
                st.success("Senha atualizada com sucesso")
        else:
            nome = st.text_input("Nome", cliente.nome)
            email = st.text_input("E-mail", cliente.email)
            fone = st.text_input("Fone", cliente.fone)
            senha = st.text_input("Senha", cliente.senha, type="password")
            if st.button("Atualizar"):
                View.cliente_atualizar(cliente.id, nome, email, fone, senha)
                st.success("Dados atualizados com sucesso")