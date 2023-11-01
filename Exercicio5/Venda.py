from Transacao import Transacao


class Venda(Transacao):
    def __init__(self, dataVenda, cliente, produto, qtdeVendida):
        super().__init__(dataVenda, produto, qtdeVendida)
        self.__cliente = cliente

# Chama o metodo verificarEstoqueInsuficiente do produto recebido por parametro passando a quantidade vendida,
# caso True, retorna uma mensagem e retorna False. Do contrário chama o metodo debitarEstoque do produto passando
# a quantidade vendida. Depois chama o metodo verificarEstoqueBaixo do produto, se True envia uma mensagem e
# retorna True.
    def vender(self, produto, qtdeVendida):
        if produto.verificarEstoqueInsuficiente(qtdeVendida):
            print("Estoque insuficiente")
            return False
        else:
            produto.debitarEstoque(qtdeVendida)
            print(f"Valor venda = {produto.calcularValorVenda(qtdeVendida)}")
            if produto.verificarEstoqueBaixo():
                print(f"Estoque baixo")
        return True
