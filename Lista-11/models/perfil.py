import json

class Perfil:
    def _init_(self, id, nome, descricao, beneficios):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.beneficios = beneficios

    def _str_(self):
        return f"{self.nome} - {self.descricao} - Benefícios: {self.beneficios}"
    
class Perfis:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = max([p.id for p in cls.objetos], default=0)
        obj.id = m + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for p in cls.objetos:
            if p.id == id:
                return p
        return None

    @classmethod
    def salvar(cls):
        with open("perfis.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("perfis.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    p = Perfil(obj["id"], obj["nome"], obj["descricao"], obj["beneficios"])
                    cls.objetos.append(p)
        except FileNotFoundError:
            pass