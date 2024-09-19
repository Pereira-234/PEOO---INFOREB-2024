import json


class Jogador:
    def __init__(self, id, nome, numeroCam, idade):
        self.id = id
        self.nome = nome
        self.numeroCam = numeroCam
        self.idade = idade
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.numeroCam} - {self.idade}"
    
class Jogadores:
    objetos = []    # atributo estático

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.objetos:
            if c.id > m: m = c.id
        obj.id = m + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.objetos:
            if c.id == id: return c
        return None  
  
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.nome = obj.nome
            c.idade = obj.idade
            c.numeroCam = obj.numeroCam
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            cls.objetos.remove(c)
            cls.salvar()
  
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def salvar(cls):
        with open("jogadores.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, default = vars)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("jogadores.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
            for obj in texto:   
                c = Jogador(obj["id"], obj["nome"], obj["numeroCam"], obj["idade"])
                cls.objetos.append(c)
        except FileNotFoundError:
            pass