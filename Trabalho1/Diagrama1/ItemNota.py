from Produto import Produto
from Nota import Nota

class ItemNota:
    def __init__(self):
        self.__id = 0
        self.__vrUnitario = 0
        self.__quantidade = 0
        self.__nota = Nota()
        self.__produto = Produto()
        self.__nota.get_itens().append(self)

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_vrUnitario(self):
        return self.__vrUnitario

    def set_vrUnitario(self, vrUnitario):
        self.__vrUnitario = vrUnitario

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        self.__nota = nota

    def get_produto(self):
        return self.__produto

    def set_produto(self, produto):
        self.__produto = produto
