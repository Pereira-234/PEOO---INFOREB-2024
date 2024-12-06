from templates.manterclienteUI import ManterClienteUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterprofissionalUI import ManterProfissionalUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.abrircontaUI import AbrirContaUI
from templates.listarhorarioUI import ListarHorarioUI
from templates.loginUI import LoginUI
from templates.vizualizaragendaprofissionalUI import VisualizarAgendaProfissionalUI
from templates.alterardadosUI import AlterarDadosUI
from views import View

import streamlit as st

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
               
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Profissionais", "Cadastro de Serviços", "Abrir Agenda do Dia"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Horários Disponíveis", "Alterar Meus Dados"])
        if op == "Horários Disponíveis": ListarHorarioUI.main()
        if op == "Alterar Meus Dados": AlterarDadosUI.main()

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Minha Agenda", "Sair"])
        if op == "Minha Agenda":
            VisualizarAgendaProfissionalUI.main()
        if op == "Sair":
            IndexUI.sair_do_sistema()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            st.rerun()
    
    def sidebar():
        if "cliente_id" not in st.session_state:
            # usuário não está logado
            IndexUI.menu_visitante()   
        else:
            admin = st.session_state["cliente_nome"] == "admin"
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_cliente()
            # usuário está logado, verifica se é o admin
            admin = st.session_state["cliente_nome"] == "admin"
            # mensagen de bem-vindo
            st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
            # menu do usuário
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_cliente()
            # controle de sair do sistema
            IndexUI.sair_do_sistema() 
            if "cliente_id" in st.session_state:
                is_profissional = st.session_state.get("is_profissional", False)
                if is_profissional:
                    IndexUI.menu_profissional()
                else:
                    admin = st.session_state["cliente_nome"] == "admin"
                    if admin: IndexUI.menu_admin()
                    else: IndexUI.menu_cliente()
    
    def main():
        # verifica a existe o usuário admin
        View.cliente_admin()
        # monta o sidebar
        IndexUI.sidebar()
       
IndexUI.main()
