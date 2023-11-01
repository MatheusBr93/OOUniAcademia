from Cliente import Cliente
from Fornecedor import Fornecedor
from Produto import Produto

def main():
    cliente1 = Cliente("Marco", "123")
    produto1 = Produto("Caneta", 100, 1.2, 10, 200)
    produto1.vender("26/07/2021", cliente1, 95)
    fornecedor1 = Fornecedor("Antonio", "456")
    produto1.comprar("26/07/2021", fornecedor1, 50, 1.1)
    produto1.exibirHistorico()


if __name__ == "__main__":
    main()