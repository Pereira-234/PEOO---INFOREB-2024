import streamlit as st
from views import View

class VisualizarAgendaProfissionalUI:
    def main():
        st.header("Minha Agenda")
        profissional_id = st.session_state["cliente_id"]
        agenda = View.profissional_listar_agenda(profissional_id)

        if not agenda:
            st.write("Nenhum horário agendado.")
        else:
            for horario in agenda:
                st.write(f"Data: {horario['data']}, Cliente: {horario['cliente']}, Serviço: {horario['servico']}")