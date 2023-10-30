from Cliente import Cliente

class Veiculo:
    def __init__(self, placa, valor):
        self.__placa = placa
        self.__valor = valor
        self.__alugado = False
        self.__cliente = Cliente
        self.__dias = 0
        self.__historico = []
    def setPlaca(self, placa):
        self.__placa = placa
        return print(f"Placa definida como: {self.__placa}")
    def getPlaca(self):
        return self.__placa

    def setValor(self, valor):
        self.__valor = valor
        return print(f"Valor definido como: {self.__valor}")

    def getValor(self):
        return self.__valor

    def setAlugado(self, alugado):
        self.__alugado = alugado

    def getAlugado(self):
        return self.__alugado


    def alugar(self, Cliente, dias):
        if not self.__alugado:
            self.__alugado = True
            self.__dias = dias
            self.__cliente = Cliente
            self.__historico.append(self.__cliente)
            return print(f"Veículo de placa {self.__placa} alugado com sucesso pelo cliente {self.__cliente} por {self.__dias} dias")
        else:
            return print(f"Veículo de placa {self.__placa} ja se encontra alugado")

    def devolver(self):
        if self.__alugado:
            self.__alugado = False
            self.__dias = 0
            self.__cliente = "Não está sendo alugado por ninguém"
            return print(f"Veículo de placa {self.__placa} devolvido com sucesso")
        else:
            return print(f"Veículo de placa {self.__placa} não pode ser devolvido, pois não se encontra alugado")


    def listarHistorico(self):
        return print(f"Histórico do veículo de placa: {self.__placa}: {[str(cliente) for cliente in self.__historico]}")