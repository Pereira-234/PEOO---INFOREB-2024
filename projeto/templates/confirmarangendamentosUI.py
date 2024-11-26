import streamlit as st
import pandas as pd
from views import View

class ConfirmarAgendamentosUI:
    def main():
        st.header("Confirmar Agendamentos")
        ConfirmarAgendamentosUI.listar_agendamentos()

    def listar_agendamentos():
        agendamentos = [h for h in View.horario_listar() if h.confirmado]
        if not agendamentos:
            st.write("Nenhum agendamento pendente de confirmação.")
        else:
            dic = []
            for agendamento in agendamentos:
                dic.append({"ID": agendamento.id, "Data": agendamento.data, "Cliente": agendamento.id_cliente, "Serviço": agendamento.id_servico})
            df = pd.DataFrame(dic)
            st.dataframe(df)
            
            selected_id = st.selectbox("Selecione o ID do agendamento para confirmar", df["ID"])
            if st.button("Confirmar Agendamento"):
                horario = View.horario_listar_id(selected_id)
                if horario:
                    horario.confirmado = True
                    View.horario_atualizar(horario.id, horario.data, horario.confirmado, horario.id_cliente, horario.id_servico)
                    st.success("Agendamento confirmado com sucesso!")