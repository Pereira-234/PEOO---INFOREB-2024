# Lista de Clientes
# C - Create - Insere um objeto na lista
# R - Read   - Listar os objetos da lista
# U - Update - Atualizar um objeto na lista
# D - Delete - Exclui um objeto da lista

import json

# Modelo
class Cliente:
    def _init_(self):
        self.__id = 0
        self.__nome = ""
        self.__email = ""
        self.__fone = ""
        self.__senha = ""

    # Métodos SET com validações
    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        if nome.strip():
            self.__nome = nome
        else:
            raise ValueError("O nome não pode ser vazio")

    def set_email(self, email):
        if email.strip():
            self.__email = email
        else:
            raise ValueError("O email não pode ser vazio")

    def set_fone(self, fone):
        if fone.strip():
            self.__fone = fone
        else:
            raise ValueError("O telefone não pode ser vazio")

    def set_senha(self, senha):
        if senha.strip():
            self.__senha = senha
        else:
            raise ValueError("A senha não pode ser vazia")

    # Métodos GET
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_fone(self):
        return self.__fone

    def get_senha(self):
        return self.__senha

    def _str_(self):
        return f"{self._nome} - {self.email} - {self._fone}"

# Persistência
class Clientes:
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
      c.email = obj.email
      c.fone = obj.fone
      c.senha = obj.senha
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
    cls.objetos.sort(key=lambda cliente: cliente.nome)
    return cls.objetos

  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:
        json.dump(
            [ {"id": c.get_id(), "nome": c.get_nome(), "email": c.get_email(), "fone": c.get_fone(), "senha": c.get_senha()} for c in cls.objetos ],
            arquivo,
        )

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("clientes.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:
            c = Cliente()
            c.set_id(obj["id"])
            c.set_nome(obj["nome"])
            c.set_email(obj["email"])
            c.set_fone(obj["fone"])
            c.set_senha(obj["senha"])
            cls.objetos.append(c)
    except FileNotFoundError:
      pass
