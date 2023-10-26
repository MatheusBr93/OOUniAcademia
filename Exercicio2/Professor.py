from Pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self):
        super().__init__()
        self.__titulacao = ""


    def setTitulacao(self,titulacao):
        self.__titulacao = titulacao
        return print("Titulação definida: " + self.__titulacao)

    def getTitulacao(self):
        return self.__titulacao

    def __str__(self):
        return f"Nome: {self.getNome()}, Titulação: {self.getTitulacao()}"
