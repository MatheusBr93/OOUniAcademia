from Pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self):
        super().__init__()
        self.__matricula = 0
        self.__nota = []


    def setMatricula(self, matricula):
        self.__matricula = matricula
        return print(f"Matrícula definida: {self.__matricula}")


    def getMatricula(self):
        return self.__matricula

    def setNota(self, nota):
        self.__nota.append(nota)
        contador = len(self.__nota)
        nota_adicionada = self.__nota[-1]
        print(f"Nota{contador} definida como: {nota_adicionada}")

    def getNota(self):
        return self.__nota

