from datetime import date
from Empresa import Empresa
from Participante import Participante

class Nota:
    def __init__(self):
        self.__id = 0
        self.__data = date.today()
        self.__numero = 0
        self.__itens = []
        self.__empresa = Empresa()
        self.__participante = Participante()

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_data(self):
        return self.__data

    def set_data(self, nova_data):
        self.__data = nova_data

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_itens(self):
        return self.__itens

    def get_empresa(self):
        return self.__empresa

    def set_empresa(self, empresa):
        self.__empresa = empresa

    def get_participante(self):
        return self.__participante

    def set_participante(self, participante):
        self.__participante = participante

    def getVrTotal(self):
        total = 0
        for item in self.__itens:
            total += item.get_vrUnitario() * item.get_quantidade()
        return total
