import json
from datetime import datetime
from datetime import timedelta
# Modelo
class Treino:
    def __init__(self, id, descricao, distancia, tempo):
        self.id = id
        self.descricao = descricao
        self.distancia = distancia
        self.tempo = tempo

    def __str__(self):
        return f"{self.id} - {self.descricao} - {self.distancia} - {self.tempo}"

    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["descricao"] = self.descricao
        dic["distancia"] = self.distancia
        dic["tempo"] = datetime



class Treinos:
    l_treinos = []    # atributo estático
    @classmethod
    def inserir(cls, treino):
        cls.abrir()
        m = 0
        for t in cls.treinos:
            if t.id > m: m = t.id
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
            if t.id == id: return t
        return None

    @classmethod
    def MaisRapido(cls):
        l_treinos.sort(key=lambda t: t.distancia / t.tempo.total_seconds(), reverse = True)
        return cls.l_treinos


    @classmethod
    def atualizar(cls, treino):
        t = cls.listar_id(treino.id)
        if t != None:
            t.descricao = treino.descricao
            t.distancia = treino.distancia
            t.tempo = treino.tempo
            cls.salvar()

    @classmethod
    def excluir(cls, treino):
        t = cls.listar_id(treino.id)
        if t != None:
            cls.treinos.remove(t)
        cls.salvar()

    @classmethod
    def abrir(cls):
        cls.treinos = []
        try:
            with open("treinos.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for treino in texto:
                    t = Treino(treino["id"], treino["descricao"], treino["distancia"], treino["tempo"])
                    cls.treinos.append(t)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("treinos.json", mode="w") as arquivo:   # w - write
            json.dump(cls.treinos, arquivo, default = Treino.to_json)

class UI:
    @staticmethod
    def main():
        op=0
        while op != 6:
            op = UI.menu()
            if op == 1: UI.treino_listar()
            if op == 2: UI.treino_inserir()
            if op == 3: UI.treino_atualizar()
            if op == 4: UI.treino_excluir()
            if op == 5: UI.treino_MaisRapido()
        

    @staticmethod
    def menu():
        print("1 - listar treino, 2 - inserir treino, 3 - atualizar treino, 4 - excluir treino, 5 - saber o treino mais rapido, 6 - finalizar operação")
        return int(input("Digite o número da operação desejada: "))

    @staticmethod
    def treino_listar():
        for t in Treinos.listar():
            print(t)

    @staticmethod
    def treino_inserir():
        id = int(input("ID do treino: "))
        descricao = input("Descrição do trteino: ")
        distancia = float(input("Distancia em Km: "))
        minutos = int(input("Tempo em minutos: "))
        segundos = int(input("Tempo em segundos: "))
        tempo = timedelta(minutes=minutos , seconds=segundos)
        treino = Treino(id, descricao, distancia, tempo)
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
            print("treino não encontrado.")

    @staticmethod
    def treino_excluir():
        UI.paciente_listar()
        id = int(input("Digite o ID do treino que será excluído: "))
        t = Treino(id, "", "", "")
        Treinos.excluir(t)

    staticmethod
    def treino_MaisRapido():
        treinos = Treinos.MaisRapido()
        if not treinos:
            print("Nenhum treino encontrado")
        else:
            print(treinos)


UI.main()