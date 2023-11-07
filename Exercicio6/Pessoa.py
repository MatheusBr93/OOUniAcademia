class Pessoa:
    def __init__(self, sexo, peso, altura):
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura

    def calcularIMC(self):
        imc= self.__peso/(self.__altura**2)
        if self.__sexo == "Masculino":
            if imc < 20.7:
                return "Abaixo do Peso"
            elif 20.7 <= imc < 26.4:
                return "Peso normal"
            elif 26.4 <= imc < 27.8:
                return "Marginalmente Acima do Peso"
            elif 27.8 <= imc < 31.1:
                return "Acima do Peso Ideal"
            else:
                return "Obeso"
        elif self.__sexo == "Feminino":
            if imc < 19.1:
                return "Abaixo do Peso"
            elif 19.1 <= imc < 25.8:
                return "Dentro do Padrão"
            elif 25.8 <= imc < 27.3:
                return "Marginalmente Acima do Peso"
            elif 27.3 <= imc < 32.3:
                return "Acima do Peso"
            else:
                return "Obesa"
        else:
            return "Sexo não reconhecido"


