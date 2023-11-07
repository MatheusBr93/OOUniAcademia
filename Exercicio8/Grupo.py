class Grupo:
    def __init__(self, grupo):
        self.__grupo = grupo
        self.__presidente = ""

    def setPresidente(self, presidente):
        self.__presidente = presidente

    def getPresidente(self):
        return self.__presidente

    def getGrupo(self):
        return self.__grupo
