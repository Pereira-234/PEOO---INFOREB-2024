from models.cliente import Cliente, Clientes
from models.horario import Horario, Horarios
from models.servico import Servico, Servicos
from models.profissional import Profissional, Profissionais
from models.perfil import Perfil, Perfis
from datetime import datetime, timedelta

class View:
    def cliente_admin():
        for c in View.cliente_listar():
            if c.email == "admin": return
        View.cliente_inserir("admin", "admin", "1234", "1234")

    def cliente_inserir(nome, email, fone, senha):
        c = Cliente(0, nome, email, fone, senha)
        Clientes.inserir(c)

    def cliente_listar():
        return Clientes.listar()    

    def cliente_listar_id(id):
        return Clientes.listar_id(id)    

    def cliente_atualizar(id, nome, email, fone, senha):
        c = Cliente(id, nome, email, fone, senha)
        Clientes.atualizar(c)

    def cliente_excluir(id):
        c = Cliente(id, "", "", "", "")
        Clientes.excluir(c)    


    def profissional_inserir(nome, especialidade, conselho):
        c = Profissional(0, nome, especialidade, conselho)
        Profissionais.inserir(c)

    def profissional_listar():
        return Profissionais.listar()    

    def profissional_listar_id(id):
        return Profissionais.listar_id(id)    

    def profissional_atualizar(id, nome, especialidade, conselho):
        c = Profissional(id, nome, especialidade, conselho)
        Profissionais.atualizar(c)

    def profissional_excluir(id):
        c = Profissional(id, "", "", "")
        Profissionais.excluir(c) 

    def profissional_adicionar_horario(id_profissional, horario):
        profissional = Profissionais.listar_id(id_profissional)
        if profissional:
            profissional.agenda.append(horario)
            Profissionais.atualizar(profissional)

    def profissional_listar_agenda(id_profissional):
        profissional = Profissionais.listar_id(id_profissional)
        if not profissional or not profissional.agenda:
            return []

        agenda_detalhada = []
        for horario in profissional.agenda:
            cliente = View.cliente_listar_id(horario["id_cliente"])
            servico = View.servico_listar_id(horario["id_servico"])
            agenda_detalhada.append({
                "data": horario["data"],
                "cliente": cliente.nome if cliente else "Não definido",
                "servico": servico.descricao if servico else "Não definido"
            })
        return agenda_detalhada



    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.email == email and c.senha == senha:
                return {"id" : c.id, "nome" : c.nome }
        return None
    
    def cliente_atualizar_perfil(id, perfil):
        cliente = Clientes.listar_id(id)
        if cliente:
            cliente.perfil = perfil
            Clientes.atualizar(cliente)

    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(0, data)
        c.confirmado = confirmado
        c.id_cliente = id_cliente
        c.id_servico = id_servico
        c.id_profissional = id_profissional
        Horarios.inserir(c)

    def horario_listar():
        return Horarios.listar()    

    def horario_listar_disponiveis():
        horarios = View.horario_listar()
        disponiveis = []
        for h in horarios:
            if h.data >= datetime.now() and h.id_cliente == None: disponiveis.append(h)
        return disponiveis   

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(id, data)
        c.confirmado = confirmado
        c.id_cliente = id_cliente
        c.id_servico = id_servico
        c.id_profissional = id_profissional
        Horarios.atualizar(c)

    def horario_excluir(id):
        c = Horario(id, None)
        Horarios.excluir(c)    

    def horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo):
        #data = "05/11/2024"
        #inicio = "08:00"
        #fim = "12:00"
        #intervalo = 60
        i = data + " " + hora_inicio   # "05/11/2024 08:00"
        f = data + " " + hora_fim      # "05/11/2024 12:00"
        d = timedelta(minutes=intervalo)
        di = datetime.strptime(i, "%d/%m/%Y %H:%M")
        df = datetime.strptime(f, "%d/%m/%Y %H:%M")
        x = di
        while x <= df:
            #cadastrar o horário x
            View.horario_inserir(x, False, None, None, None)
            #passar para o próximo horário
            x = x + d

    def servico_inserir(descricao, valor, duracao):
        c = Servico(0, descricao, valor, duracao)
        Servicos.inserir(c)

    def servico_listar():
        return Servicos.listar()    

    def servico_listar_id(id):
        return Servicos.listar_id(id)    

    def servico_atualizar(id, descricao, valor, duracao):
        c = Servico(id, descricao, valor, duracao)
        Servicos.atualizar(c)

    def servico_excluir(id):
        c = Servico(id, "", 0, 0)
        Servicos.excluir(c)

    def perfil_inserir(nome, descricao, beneficios):
        p = Perfil(0, nome, descricao, beneficios)
        Perfis.inserir(p)

    def perfil_listar():
        return Perfis.listar()

    def cliente_atualizar_perfil(id_cliente, id_perfil):
        cliente = Clientes.listar_id(id_cliente)
        if cliente:
            cliente.idPerfil = id_perfil
            Clientes.atualizar(cliente)