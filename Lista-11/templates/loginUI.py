import streamlit as st
from views import View
import time

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        profissional = View.profissional_listar_id(email)
        if profissional and profissional.senha == senha:
            st.session_state["cliente_id"] = profissional.id
            st.session_state["cliente_nome"] = profissional.nome
            st.session_state["is_profissional"] = True
            st.rerun()
        if st.button("Entrar"):
            cliente = View.cliente_autenticar(email, senha)
            if cliente:
                st.session_state["cliente_id"] = cliente["id"]
                st.session_state["cliente_nome"] = cliente["nome"]
                # Verifica se é profissional
                profissional = View.profissional_listar_id(cliente["id"])
                st.session_state["is_profissional"] = profissional is not None
                st.rerun()
            else:
                st.write("E-mail ou senha inválidos")