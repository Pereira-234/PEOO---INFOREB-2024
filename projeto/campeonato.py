import json
from times import Times  

class Campeonato:
    def __init__(self, id, nome, descricao, patrocinadores=None, times=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.patrocinadores = patrocinadores 
        self.times = times if times is not None else []

    def __str__(self):
        times_str = ", ".join([str(time_id) for time_id in self.times])
        return (f"Campeonato ID: {self.id} - Nome: {self.nome} - Descrição: {self.descricao} - "
                f"Patrocinadores: [{self.patrocinadores}] - Times IDs: [{times_str}]")

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "patrocinadores": self.patrocinadores,
            "times": self.times
        }

class Campeonatos:
    campeonatos = []  

    @classmethod
    def inserir(cls, campeonato):
        cls.abrir()
        m = max((c.id for c in cls.campeonatos), default=0)
        campeonato.id = m + 1
        cls.campeonatos.append(campeonato)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.campeonatos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.campeonatos:
            if c.id == id:
                return c
        return None

    @classmethod
    def atualizar(cls, campeonato_id, nome=None, descricao=None, patrocinadores=None, times=None):
        campeonato = cls.listar_id(campeonato_id)
        if campeonato:
            if nome:
                campeonato.nome = nome
            if descricao:
                campeonato.descricao = descricao
            if patrocinadores:
                campeonato.patrocinadores = patrocinadores
            if times:
                campeonato.times = times
            cls.salvar()
            return True
        return False

    @classmethod
    def excluir(cls, campeonato):
        c = cls.listar_id(campeonato.id)
        if c is not None:
            cls.campeonatos.remove(c)
            cls.salvar()

    @classmethod
    def adicionar_time_ao_campeonato(cls, campeonato_id, time_id):
        campeonato = cls.listar_id(campeonato_id)
        time = Times.listar_id(time_id)
        if campeonato and time and time_id not in campeonato.times:
            campeonato.times.append(time_id)
            cls.salvar()
            return True
        return False

    @classmethod
    def abrir(cls):
        cls.campeonatos = []
        try:
            with open("campeonatos.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for campeonato in texto:
                    c = Campeonato(campeonato["id"], campeonato["nome"], campeonato["descricao"],
                                   campeonato["patrocinadores"], campeonato["times"])
                    cls.campeonatos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("campeonatos.json", mode="w") as arquivo:
            json.dump(cls.campeonatos, arquivo, default=Campeonato.to_json)
