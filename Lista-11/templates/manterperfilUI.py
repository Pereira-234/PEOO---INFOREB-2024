import streamlit as st
from views import View

class ManterPerfilUI:
    def main():
        st.header("Cadastro de Perfis")
        tab1, tab2 = st.tabs(["Listar", "Inserir"])
        with tab1: ManterPerfilUI.listar()
        with tab2: ManterPerfilUI.inserir()

    def listar():
        perfis = View.perfil_listar()
        if not perfis:
            st.write("Nenhum perfil cadastrado")
        else:
            for p in perfis:
                st.write(f"{p.id} - {p.nome} - {p.descricao} - Benefícios: {p.beneficios}")

    def inserir():
        nome = st.text_input("Nome do Perfil")
        descricao = st.text_input("Descrição do Perfil")
        beneficios = st.text_input("Benefícios")
        if st.button("Inserir"):
            View.perfil_inserir(nome, descricao, beneficios)
            st.success("Perfil inserido com sucesso")
            st.rerun()