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
