from Carro import Carro
from Moto import Moto
from Cliente import Cliente


def main():
        cliente1 = Cliente()
        cliente2 = Cliente()
        cliente3 = Cliente()
        cliente1.setNome("Vitor")
        cliente2.setNome("Felipe")
        cliente3.setNome("Pedro")
        print("*************************")
        carro1 = Carro("HB20", "123ABC", 30)
        carro2 = Carro("Gol Bolinha", "ABC123", 50)
        moto1 = Moto("VRUM123", 40)

        carro1.alugar(cliente1, 20)
        carro1.devolver()
        carro1.alugar(cliente2, 40)
        carro1.devolver()
        carro1.alugar(cliente3, 60)
        print("*************************")
        carro2.alugar(cliente2, 20)
        carro2.devolver()
        carro2.alugar(cliente3, 40)
        carro2.devolver()
        carro2.alugar(cliente1, 60)
        carro2.alugar(cliente3, 20)
        print("*************************")
        moto1.alugar(cliente3, 20)
        moto1.devolver()
        moto1.alugar(cliente1, 40)
        moto1.devolver()
        moto1.alugar(cliente2, 60)

        print("*************************")
        carro1.listarHistorico()
        carro2.listarHistorico()
        moto1.listarHistorico()
        print("*************************")
        carro1.calcularAluguel(20)
        carro1.calcularAluguel(40)
        carro1.calcularAluguel(60)
        carro2.calcularAluguel(20)
        carro2.calcularAluguel(40)
        carro2.calcularAluguel(60)
        moto1.calcularAluguel(20)
        moto1.calcularAluguel(40)
        moto1.calcularAluguel(60)


if __name__ == "__main__":
    main()