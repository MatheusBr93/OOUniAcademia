from TipoEnsino import TipoEnsino
from Escola import Escola
from Professor import Professor
class Curso:
    def __init__(self):
        self.__nome = ""
        self.__tipoensino = TipoEnsino()
        self.__alunos = []
        self.__professores = []
        self.__escola = Escola()
        self.__coordenador = ""
        self.__professor = Professor()

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setCoordenador(self, professor):
        self.__coordenador = professor

    def getCoordenador(self):
        return self.__coordenador

    def setEscola(self, escola):
        self.__escola = escola

    def getEscola(self):
        return self.__escola

    def setTipodeEnsino(self, tipodeensino):
        self.__tipoensino = tipodeensino

    def getTipodeEnsino(self):
        return self.__tipoensino

