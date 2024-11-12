import streamlit as st
import pandas as pd
from views import View

class ListarHorarioUI:
    def main():
        st.header("Horários Disponíveis")
        ListarHorarioUI.listar()

    def listar():
        horarios = View.horario_listar_disponiveis()
        if len(horarios) == 0:
            st.write("Nenhum horário disponível")
        else:
            dic = []
            for obj in horarios:
                horario_data = obj.to_json()
                horario_data.pop("id_cliente", None)
                horario_data.pop("id_servico", None)
                dic.append(horario_data)
            df = pd.DataFrame(dic)
            st.dataframe(df)
            
            selected_index = st.selectbox("Selecione um horário para agendar", range(len(horarios)))
            cliente_id = st.session_state.get("cliente_id")
            servico_id = st.text_input("Informe o ID do serviço que deseja agendar")
            if st.button("Agendar Serviço"):
                if cliente_id and servico_id:
                    horario = horarios[selected_index]
                    View.horario_atualizar(horario.id, horario.data, True, cliente_id, int(servico_id))
                    st.success("Serviço agendado com sucesso!")
                else:
                    st.error("Por favor, informe o ID do serviço.")