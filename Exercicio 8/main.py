from Pais import Pais
from Estado import Estado
from Cidade import Cidade
from Filial import Filial
from Funcionario import Funcionario
from Grupo import Grupo
from Escolaridade import Escolaridade
from Departamento import Departamento
from Empresa import Empresa

escolaridade1 = Escolaridade("Ensino Médio completo")
empresa1 = Empresa("Empresa 1")
pais1 = Pais("Brasil")
estado1 = Estado("Rio de Janeiro")
cidade1 = Cidade("Nova Iguaçu")
filial1 = Filial("Filial 1")
funcionario1 = Funcionario("Vitor", escolaridade1, empresa1)
grupo1 = Grupo("Grupo 1")
departamento1 = Departamento("Departamento 1")


empresa1.setDiretor(funcionario1)
pais1.setSede(estado1)
estado1.adicionarCidade(cidade1)
cidade1.adicionarFilial(filial1)
filial1.setEmpresa(empresa1)
filial1.adicionarFuncionario(funcionario1)
empresa1.adicionarDepartamento(departamento1)
grupo1.setPresidente(funcionario1)
departamento1.setChefe(funcionario1)

print(f'1- A escolaridade do presidente |{grupo1.getPresidente().getNome()}| é |{grupo1.getPresidente().getEscolaridade().getEscolaridade()}|')
print(f'2- O país de alocação do funcionário |{funcionario1.getNome()}| é o |{pais1.getNome()}|')
print(f'3- O Estado da filial |{filial1.getNome()}| do coordenador |{departamento1.getChefe().getNome()}| é o Estado do |{estado1.getNome()}|')
print(f'4- A escolaridade do chefe |{departamento1.getChefe().getNome()}| do departamento |{departamento1.getDepartamento()}| é |{departamento1.getChefe().getEscolaridade().getEscolaridade()}|')
print(f'5- O nome do diretor da empresa |{empresa1.getNome()}| que está na filial |{filial1.getNome()}| é o |{empresa1.getDiretor().getNome()}|')
