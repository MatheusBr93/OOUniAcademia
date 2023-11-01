from Venda import Venda
from Compra import Compra
class Produto:
    def __init__(self, nome, qtdeEstoque, precoUnit, estoqueMinimo, estoqueMaximo):
        self.__nome = nome
        self.__qtdeEstoque = qtdeEstoque
        self.__precoUnit = precoUnit
        self.__estoqueMaximo = estoqueMaximo
        self.__estoqueMinimo = estoqueMinimo
        self.__historico = []

#Retorna o nome do produto
    def getNome(self):
        return self.__nome

#Diminui o estoque de acordo com o parametro
    def debitarEstoque(self, quantidade):
        self.__qtdeEstoque -= quantidade

#Aumenta o estoque de acordo com o parametro
    def creditarEstoque(self, quantidade):
        self.__qtdeEstoque += quantidade

#Retorna True caso o estoque atual for abaixo do minimo, retorna False o contrario
    def verificarEstoqueBaixo(self):
        if self.__qtdeEstoque < self.__estoqueMinimo:
            return True
        else:
            return False

#Retona True caso a quantidade do parametro for superior ao estoque atual, retorna False o contrario
    def verificarEstoqueInsuficiente(self, quantidade):
        if quantidade > self.__qtdeEstoque:
            return True
        else:
            return False

#Retorna True se a quantidade somada ao estoque for superior ao estoque maximo, retorna False o contrario
    def verificarEstoqueExcedente(self, quantidade):
        if quantidade + self.__qtdeEstoque > self.__estoqueMaximo:
            return True
        else:
            return False

#Retorna a multiplicação do preço unitario pela quantidade recebida pelo parametro
    def calcularValorVenda(self, quantidade):
        return self.__precoUnit * quantidade

#Instancia um objeto do tipo Venda e chama o metodo vender do novo objeto, caso True a venda é registrada no historico
    def vender(self, dataVenda, cliente, qtdeVendida):
        vendax = Venda(dataVenda, cliente, self, qtdeVendida)
        if vendax.vender(self, qtdeVendida):
            self.registrarHistorico(f"Venda do produto {self.getNome()}")

#Instancia um objeto do tipo Compra e chama o metodo comprar do novo objeto, caso True a compra é registrada no historico
    def comprar(self, dataCompra, fornecedor, qtdeCompra, precoUnit):
        comprax = Compra(dataCompra, self, fornecedor, qtdeCompra, precoUnit)
        if comprax.comprar(self, qtdeCompra):
            self.registrarHistorico(f"Compra do produto {self.getNome()}")

#Registra a compra/venda na lista de historicos
    def registrarHistorico(self, transacao):
        self.__historico.append(transacao)

#Imprime a lista de historicos
    def exibirHistorico(self):
        for historico in self.__historico:
            print(historico)



