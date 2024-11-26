import streamlit as st
from views import View

class PerfilUsuarioUI:
    def main():
        st.header("Perfil do Usuário")
        if "cliente_id" in st.session_state:
            usuario = View.cliente_listar_id(st.session_state["cliente_id"])
            if st.session_state["cliente_nome"] == "admin":
                senha = st.text_input("Nova senha para o Admin", type="password")
                confirm_senha = st.text_input("Confirme a nova senha", type="password")
                if st.button("Atualizar Senha"):
                    if senha == confirm_senha:
                        View.cliente_atualizar(usuario.id, usuario.nome, usuario.email, usuario.fone, senha)
                        st.success("Senha do Admin atualizada com sucesso")
                    else:
                        st.error("As senhas não coincidem")
            else:
                nome = st.text_input("Nome", usuario.nome)
                email = st.text_input("E-mail", usuario.email)
                fone = st.text_input("Fone", usuario.fone)
                senha = st.text_input("Nova senha", type="password")
                confirm_senha = st.text_input("Confirme a nova senha", type="password")
                if st.button("Atualizar Perfil"):
                    if senha == confirm_senha:
                        View.cliente_atualizar(usuario.id, nome, email, fone, senha)
                        st.success("Perfil atualizado com sucesso")
                    else:
                        st.error("As senhas não coincidem")