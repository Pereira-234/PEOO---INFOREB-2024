from models.cliente import Cliente, Clientes
from models.horario import Horario, Horarios
from models.servico import Servico, Servicos
from models.profissional import Profissional, Profissionais
from datetime import datetime, timedelta

class View:
    def cliente_admin():
        for c in View.cliente_listar():
            if c.email == "admin": return
        View.cliente_inserir("admin", "admin", "1234", "1234")

    def cliente_inserir(nome, email, fone, senha):
    # Verificar se o email já existe
    for cliente in View.cliente_listar():
        if cliente.get_email() == email:
            raise ValueError(f"Já existe um cliente com o email '{email}'.")
    c = Cliente()
    c.set_nome(nome)
    c.set_email(email)
    c.set_fone(fone)
    c.set_senha(senha)
    Clientes.inserir(c)

    def cliente_listar():
        return Clientes.listar()    

    def cliente_listar_id(id):
        return Clientes.listar_id(id)    

    def cliente_atualizar(id, nome, email, fone, senha):
    for cliente in View.cliente_listar():
        if cliente.get_email() == email and cliente.get_id() != id:
            raise ValueError(f"Já existe um cliente com o email '{email}'.")
    c = Cliente()
    c.set_id(id)
    c.set_nome(nome)
    c.set_email(email)
    c.set_fone(fone)
    c.set_senha(senha)
    Clientes.atualizar(c)

   def cliente_excluir(id):
    for horario in View.horario_listar():
        if horario.get_id_cliente() == id:
            raise ValueError(f"O cliente com ID '{id}' possui horários agendados e não pode ser excluído.")
    Clientes.excluir(Cliente(id, "", "", "", ""))    

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.email == email and c.senha == senha:
                return {"id" : c.id, "nome" : c.nome }
        return None

    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
    if not View.cliente_listar_id(id_cliente):
        raise ValueError(f"O cliente com ID '{id_cliente}' não é válido.")
    if not View.servico_listar_id(id_servico):
        raise ValueError(f"O serviço com ID '{id_servico}' não é válido.")
    c = Horario()
    c.set_data(data)
    c.set_confirmado(confirmado)
    c.set_id_cliente(id_cliente)
    c.set_id_servico(id_servico)
    c.set_id_profissional(id_profissional)
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
    if not View.cliente_listar_id(id_cliente):
        raise ValueError(f"O cliente com ID '{id_cliente}' não é válido.")
    if not View.servico_listar_id(id_servico):
        raise ValueError(f"O serviço com ID '{id_servico}' não é válido.")
    c = Horario()
    c.set_id(id)
    c.set_data(data)
    c.set_confirmado(confirmado)
    c.set_id_cliente(id_cliente)
    c.set_id_servico(id_servico)
    c.set_id_profissional(id_profissional)
    Horarios.atualizar(c)
       
    def horario_excluir(id):
    horario = View.horario_listar_id(id)
    if horario.get_confirmado():
        raise ValueError(f"O horário com ID '{id}' está confirmado para um cliente e não pode ser excluído.")
    Horarios.excluir(horario)    

    def horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo):
    try:
        di = datetime.strptime(data + " " + hora_inicio, "%d/%m/%Y %H:%M")
        df = datetime.strptime(data + " " + hora_fim, "%d/%m/%Y %H:%M")
        if di >= df:
            raise ValueError("A hora inicial deve ser menor que a hora final.")
        if intervalo <= 0:
            raise ValueError("O intervalo deve ser maior que zero.")
    except ValueError as e:
        raise ValueError(f"Erro nas datas ou horários: {e}")

    d = timedelta(minutes=intervalo)
    x = di
    while x <= df:
        View.horario_inserir(x, False, None, None, None)
        x += d

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
    for horario in View.horario_listar():
        if horario.get_id_servico() == id:
            raise ValueError(f"O serviço com ID '{id}' está associado a horários agendados e não pode ser excluído.")
    Servicos.excluir(Servico(id, "", 0, 0))    

    def profissional_inserir(nome, especialidade, conselho):
        p = Profissional(0, nome, especialidade, conselho)
        Profissionais.inserir(p)

    def profissional_listar():
        return Profissionais.listar()

    def profissional_listar_id(id):
        return Profissionais.listar_id(id)

    def profissional_atualizar(id, nome, especialidade, conselho):
        p = Profissional(id, nome, especialidade, conselho)
        Profissionais.atualizar(p)

    def profissional_excluir(id):
        p = Profissional(id, "", "", "")
        Profissionais.excluir(p)

