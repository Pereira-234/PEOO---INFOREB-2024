import json
from jogador import Jogadores

class Time:
    def __init__(self, id, nome, jogadores=None):
        self.id = id
        self.nome = nome
        self.jogadores = jogadores if jogadores is not None else []

    def __str__(self):
        jogadores_str = ", ".join([str(jogador_id) for jogador_id in self.jogadores])
        return f"{self.id} - {self.nome} - Jogadores IDs: [{jogadores_str}]"

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "jogadores": self.jogadores
        }

class Times:
    times = []  

    @classmethod
    def inserir(cls, time):
        cls.abrir()
        m = max((t.id for t in cls.times), default=0)
        time.id = m + 1
        cls.times.append(time)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.times

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for t in cls.times:
            if t.id == id:
                return t
        return None

    @classmethod
    def atualizar(cls, time_id, nome=None, jogadores=None):
        time = cls.listar_id(time_id)
        if time:
            if nome:
                time.nome = nome
            if jogadores:
                time.jogadores = jogadores
            cls.salvar()
            return True
        return False

    @classmethod
    def excluir(cls, time):
        t = cls.listar_id(time.id)
        if t is not None:
            cls.times.remove(t)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.times = []
        try:
            with open("times.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for time in texto:
                    t = Time(time["id"], time["nome"], time["jogadores"])
                    cls.times.append(t)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("times.json", mode="w") as arquivo:
            json.dump(cls.times, arquivo, default=Time.to_json)

    @classmethod
    def adicionar_jogador_ao_time(cls, time_id, jogador_id):
        time = cls.listar_id(time_id)
        jogador = Jogadores.listar_id(jogador_id)
        if time and jogador and jogador_id not in time.jogadores:
            time.jogadores.append(jogador_id)
            cls.salvar()
            return True
        return False
