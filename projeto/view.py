from jogador import Jogador, Jogadores
from times import Time, Times
from campeonato import Campeonato, Campeonatos  # Importando as classes de campeonatos

# Funções para manipular Jogadores
def jogador_inserir(nome, numeroCam, idade):
    jogador = Jogador(0, nome, numeroCam, idade)
    Jogadores.inserir(jogador)

def jogador_listar():
    return Jogadores.listar()

def jogador_atualizar(id, nome=None, numeroCam=None, idade=None):
    jogador = Jogadores.listar_id(id)
    if jogador:
        jogador.nome = nome if nome is not None else jogador.nome
        jogador.numeroCam = numeroCam if numeroCam is not None else jogador.numeroCam
        jogador.idade = idade if idade is not None else jogador.idade
        Jogadores.atualizar(jogador)
        return True
    return False

def jogador_excluir(id):
    jogador = Jogador(id, "", 0, 0)
    Jogadores.excluir(jogador)

# Funções para manipular Times
def time_inserir(nome):
    time = Time(0, nome)
    Times.inserir(time)

def time_listar():
    return Times.listar()

def time_atualizar(id, nome=None, jogadores=None):
    return Times.atualizar(id, nome, jogadores)

def time_excluir(id):
    time = Time(id, "")
    Times.excluir(time)

def adicionar_jogador_ao_time(time_id, jogador_id):
    return Times.adicionar_jogador_ao_time(time_id, jogador_id)

# Funções para manipular Campeonatos
def campeonato_inserir(nome, descricao, patrocinadores=None):
    patrocinadores = patrocinadores if patrocinadores is not None else []
    campeonato = Campeonato(0, nome, descricao, patrocinadores)
    Campeonatos.inserir(campeonato)

def campeonato_listar():
    return Campeonatos.listar()

def campeonato_atualizar(id, nome=None, descricao=None, patrocinadores=None, times=None):
    return Campeonatos.atualizar(id, nome, descricao, patrocinadores, times)

def campeonato_excluir(id):
    campeonato = Campeonato(id, "", "")
    Campeonatos.excluir(campeonato)

def adicionar_time_ao_campeonato(campeonato_id, time_id):
    return Campeonatos.adicionar_time_ao_campeonato(campeonato_id, time_id)
