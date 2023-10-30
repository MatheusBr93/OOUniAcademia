from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, placa, valor):
        super().__init__(placa, valor)


    def calcularAluguel(self, dias):
        valorAluguel = self.getValor() * dias
        return print(f"Valor do aluguel veículo de placa {self.getPlaca()} por {dias} dias= {valorAluguel}")