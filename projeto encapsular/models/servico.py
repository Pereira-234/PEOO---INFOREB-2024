import json

# Modelo
class Servico:
    def _init_(self):
        self.__id = 0
        self.__descricao = ""
        self.__valor = 0.0
        self.__duracao = 0

    # Métodos SET com validações
    def set_id(self, id):
        self.__id = id

    def set_descricao(self, descricao):
        if descricao.strip():
            self.__descricao = descricao
        else:
            raise ValueError("A descrição não pode ser vazia")

    def set_valor(self, valor):
        if valor >= 0:
            self.__valor = valor
        else:
            raise ValueError("O valor não pode ser negativo")

    def set_duracao(self, duracao):
        if duracao >= 0:
            self.__duracao = duracao
        else:
            raise ValueError("A duração não pode ser negativa")

    # Métodos GET
    def get_id(self):
        return self.__id

    def get_descricao(self):
        return self.__descricao

    def get_valor(self):
        return self.__valor

    def get_duracao(self):
        return self.__duracao

    def _str_(self):
        return f"{self._id} - {self.descricao} - R$ {self.valor:.2f} - {self._duracao} min"
      
# Persistência
class Servicos:
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
      c.descricao = obj.descricao
      c.valor = obj.valor
      c.duracao = obj.duracao
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
    with open("servicos.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("servicos.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Servico(obj["id"], obj["descricao"], obj["valor"], obj["duracao"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass
