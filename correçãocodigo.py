import json
from datetime import timedelta

class Treino:
    def __init__(self, id, descricao, distancia, tempo):
        self.id = id
        self.descricao = descricao
        self.distancia = distancia
        self.tempo = tempo

    def __str__(self):
        return f"{self.id} - {self.descricao} - {self.distancia} km - {self.tempo}"

    def to_json(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "distancia": self.distancia,
            "tempo": self.tempo.total_seconds()
        }

class Treinos:
    treinos = []    # atributo estático

    @classmethod
    def inserir(cls, treino):
        cls.abrir()
        m = max((t.id for t in cls.treinos), default=0)
        treino.id = m + 1
        cls.treinos.append(treino)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.treinos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for t in cls.treinos:
            if t.id == id:
                return t
        return None

    @classmethod
    def MaisRapido(cls):
        cls.abrir()
        if not cls.treinos:
            return None
        return max(cls.treinos, key=lambda t: t.distancia / t.tempo.total_seconds())

    @classmethod
    def atualizar(cls, treino_id, descricao=None, distancia=None, tempo=None):
        treino = cls.listar_id(treino_id)
        if treino:
            if descricao:
                treino.descricao = descricao
            if distancia:
                treino.distancia = distancia
            if tempo:
                treino.tempo = tempo
            cls.salvar()
            return True
        return False

    @classmethod
    def excluir(cls, treino):
        t = cls.listar_id(treino.id)
        if t is not None:
            cls.treinos.remove(t)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.treinos = []
        try:
            with open("treinos.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for treino in texto:
                    t = Treino(treino["id"], treino["descricao"], treino["distancia"], timedelta(seconds=treino["tempo"]))
                    cls.treinos.append(t)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("treinos.json", mode="w") as arquivo:
            json.dump(cls.treinos, arquivo, default=Treino.to_json)

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = UI.menu()
            if op == 1: UI.treino_listar()
            if op == 2: UI.treino_inserir()
            if op == 3: UI.treino_atualizar()
            if op == 4: UI.treino_excluir()
            if op == 5: UI.treino_MaisRapido()
        
    @staticmethod
    def menu():
        print("1 - Listar treino, 2 - Inserir treino, 3 - Atualizar treino, 4 - Excluir treino, 5 - Saber o treino mais rápido, 6 - Finalizar operação")
        return int(input("Digite o número da operação desejada: "))

    @staticmethod
    def treino_listar():
        for t in Treinos.listar():
            print(t)

    @staticmethod
    def treino_inserir():
        descricao = input("Descrição do treino: ")
        distancia = float(input("Distância em Km: "))
        minutos = int(input("Tempo em minutos: "))
        segundos = int(input("Tempo em segundos: "))
        tempo = timedelta(minutes=minutos, seconds=segundos)
        treino = Treino(0, descricao, distancia, tempo)
        Treinos.inserir(treino)
        print("Treino inserido com sucesso!")
    
    @staticmethod
    def treino_atualizar():
        UI.treino_listar()
        id = int(input("Informe o ID do treino para atualizá-lo: "))
        descricao = input("Digite a nova descrição: ")
        distancia = input("Digite a nova distância (km): ")
        minutos = input("Digite o novo tempo em minutos: ")
        segundos = input("Digite o novo tempo em segundos: ")
        
        if distancia:
            distancia = float(distancia)
        if minutos or segundos:
            minutos = int(minutos) if minutos else 0
            segundos = int(segundos) if segundos else 0
            tempo = timedelta(minutes=minutos, seconds=segundos)
        else:
            tempo = None

        atualizado = Treinos.atualizar(id, descricao or None, distancia or None, tempo)
        if atualizado:
            print("Treino atualizado!")
        else:
            print("Treino não encontrado.")

    @staticmethod
    def treino_excluir():
        UI.treino_listar()
        id = int(input("Digite o ID do treino que será excluído: "))
        treino = Treino(id, "", 0, timedelta())
        Treinos.excluir(treino)
        print("Treino excluído com sucesso.")

    @staticmethod
    def treino_MaisRapido():
        treino = Treinos.MaisRapido()
        if not treino:
            print("Nenhum treino encontrado.")
        else:
            print(f"O treino mais rápido é: {treino}")

UI.main()
