from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo,  placa, valor):
        super().__init__(placa, valor)
        self.__modelo = modelo


    def calcularAluguel(self, dias):
        if dias <= 30:
            valorAluguel = self.getValor() * dias * 1.1
            return print(f"Valor do aluguel= {valorAluguel}")
        else:
            valorAluguel = self.getValor() * dias * 1.2
            return print(f"Valor do aluguel= {valorAluguel}")




