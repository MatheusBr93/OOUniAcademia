from Funcionario import Funcionario

funcionario1 = Funcionario()
funcionario1.setNome("Eduardo")
funcionario1.setSalarioBruto(2500.50)
funcionario1.setTotalDeAcrescimos(500.50)
funcionario1.setTotalDeDescontos(250.50)

print(f'O funcionário |{funcionario1.getNome()}| '
      f'tem de salário bruto |{funcionario1.getSalarioBruto()}|, '
      f'tem de acréscimos |{funcionario1.getTotalDeAcrescimos()}|, '
      f'tem de descontos |{funcionario1.getTotalDeDescontos()}| e '
      f'tem de salário líquido |{funcionario1.getSalarioLiquido()}|')
