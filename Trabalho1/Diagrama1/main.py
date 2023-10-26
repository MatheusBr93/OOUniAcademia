from Empresa import Empresa
from Nota import Nota
from ItemNota import ItemNota
from Produto import Produto
from Participante import Participante
from datetime import date

def main():
    empresa = Empresa()
    empresa.set_id(1)
    empresa.set_codigo("ABC123")
    empresa.set_razaoSocial("Minha Empresa")
    empresa.set_endereco("Rua Principal, 123")
    empresa.set_cnpj("1234567890")

    participante = Participante()
    participante.set_id(1)
    participante.set_codigo("XYZ456")
    participante.set_razaoSocial("Minha Participante")
    participante.set_cnpj("9876543210")

    nota = Nota()
    data_nota = date(2023, 9, 28)
    nota.set_id(1)
    nota.set_numero(123)
    nota.set_data(data_nota)
    nota.set_empresa(empresa)
    nota.set_participante(participante)

    produto = Produto()
    produto.set_id(1)
    produto.set_codigo("ABC123")
    produto.set_descricao("Produto A")

    item_nota = ItemNota()
    item_nota.set_id(1)
    item_nota.set_vrUnitario(10.0)
    item_nota.set_quantidade(5)
    nota.get_itens().append(item_nota)

    print(nota.getVrTotal())

if __name__ == "__main__":
    main()






