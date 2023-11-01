from Transacao import Transacao
class Compra(Transacao):
    def __init__(self, dataCompra, produto, fornecedor, qtdeCompra, precoUnit):
        super().__init__(dataCompra,produto, qtdeCompra)
        self.__precoUnit = precoUnit
        self.__fornecedor = fornecedor

#Chama o metodo verificarEstoqueExcedente do produto recebido por parametro, e passa a quantidade comprada, caso True exibe uma mensagem e retorna False. Do contrario chama o método creditarEstoque do produto passando a quantidade comprada e retorna True no final.
    def comprar(self, produto, qtdeCompra):
        if produto.verificarEstoqueExcedente(qtdeCompra):
            print(f"Estoque Excedido")
            return False
        else:
            produto.creditarEstoque(qtdeCompra)
            return True




