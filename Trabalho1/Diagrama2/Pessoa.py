from datetime import date

class Pessoa:
    def __init__(self):
        self.__id = 0
        self.__nome = ""
        self.__cpf = ""
        self.__dataNascimento = date.today()
        self.__email = ""
        self.__endereco = ""
        self.__telefone = ""
        self.__identidade = ""

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome

    def set_nome(self,nome):
        self.__nome = nome

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_dataNascimento(self):
        return self.__dataNascimento

    def set_dataNascimento(self, data):
        self.__dataNascimento = data

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_identidade(self):
        return self.__identidade

    def set_identidade(self, identidade):
        self.__identidade = identidade