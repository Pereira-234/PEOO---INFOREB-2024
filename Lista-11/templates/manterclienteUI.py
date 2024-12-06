import streamlit as st
import pandas as pd
from views import View
import time

class ManterClienteUI:
    def main():
        if "placeholder" not in st.session_state: 
            st.session_state["placeholder"] = ""
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()

    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:    
            #for obj in clientes: st.write(obj)
            dic = []
            for obj in clientes: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome do cliente", placeholder = st.session_state["placeholder"])
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")
        
        if st.button("Inserir"):
            if nome == "":
                st.session_state["placeholder"] = "O campo não pode estar vazio!"
                st.error("Informe o nome")
                time.sleep(2)
                st.rerun()
            else:
                View.cliente_inserir(nome, email, fone, senha)
                st.success("Cliente inserido com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de cliente", clientes)
            nome = st.text_input("Informe o novo nome do cliente", op.nome)
            email = st.text_input("Informe o novo e-mail", op.email)
            fone = st.text_input("Informe o novo fone", op.fone)
            senha = st.text_input("Informe a nova senha", op.senha, type="password")
            perfil = st.text_input("Informe o perfil do cliente", op.perfil)
            if st.button("Atualizar"):
                View.cliente_atualizar(op.id, nome, email, fone, senha, perfil)
                st.success("Cliente atualizado com sucesso")
                time.sleep(2)
                st.rerun()
        perfis = View.perfil_listar()
        perfil = st.selectbox("Selecione o perfil do cliente", perfis, format_func=lambda x: x.nome)
        View.cliente_inserir(nome, email, fone, senha, perfil.id)

            


    def excluir():
        clientes = View.cliente_listar()
        if len(clientes) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de cliente", clientes)
            if st.button("Excluir"):
                View.cliente_excluir(op.id)
                st.success("Cliente excluído com sucesso")
                time.sleep(2)
                st.rerun()