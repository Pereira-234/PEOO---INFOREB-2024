import json
from datetime import datetime

class Horario:
    def _init_(self):
        self.__id = 0
        self.__data = None
        self.__confirmado = False
        self.__id_cliente = 0
        self.__id_servico = 0
        self.__id_profissional = 0

    # Métodos SET
    def set_id(self, id):
        self.__id = id

    def set_data(self, data):
        if isinstance(data, datetime):
            self.__data = data
        else:
            raise ValueError("A data deve ser um objeto datetime")

    def set_confirmado(self, confirmado):
        self.__confirmado = confirmado

    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def set_id_servico(self, id_servico):
        self.__id_servico = id_servico

    def set_id_profissional(self, id_profissional):
        self.__id_profissional = id_profissional

    # Métodos GET
    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_confirmado(self):
        return self.__confirmado

    def get_id_cliente(self):
        return self.__id_cliente

    def get_id_servico(self):
        return self.__id_servico

    def get_id_profissional(self):
        return self.__id_profissional

    def to_json(self):
        return {
            "id": self.__id,
            "data": self._data.strftime("%d/%m/%Y %H:%M") if self._data else None,
            "confirmado": self.__confirmado,
            "id_cliente": self.__id_cliente,
            "id_servico": self.__id_servico,
            "id_profissional": self.__id_profissional,
        }

    def _str_(self):
        return f"{self._id} - {self._data}"
