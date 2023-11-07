from Pessoa import Pessoa

def main():
    pessoa1 = Pessoa("Masculino", 70, 1.75)
    resultado1 = pessoa1.calcularIMC()
    print(f"Pessoa 1: O IMC está {resultado1}")

    pessoa2 = Pessoa("Feminino", 60, 1.65)
    resultado2 = pessoa2.calcularIMC()
    print(f"Pessoa 2: O IMC está {resultado2}")

    pessoa3 = Pessoa("Masculino", 90, 1.80)
    resultado3 = pessoa3.calcularIMC()
    print(f"Pessoa 3: O IMC está {resultado3}")

if __name__ == "__main__":
    main()