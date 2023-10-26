class Empresa:
    def __init__(self):
        self.__id = 0
        self.__codigo = 0
        self.__razaoSocial = ""
        self.__endereco = ""
        self.__cnpj = ""

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_razaoSocial(self):
        return self.__razaoSocial

    def set_razaoSocial(self, razaoSocial):
        self.__razaoSocial = razaoSocial

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def get_cnpj(self):
        return self.__cnpj

    def set_cnpj(self, cnpj):
        self.__cnpj = cnpj