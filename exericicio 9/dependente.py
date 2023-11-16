from datetime import datetime

class Dependente():
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def get_idade(self, ano, mes):
        data_referencia = datetime(ano, mes, 1)
        idade = (data_referencia - self.data_nascimento).days // 365
        return idade
    def calcular_proximo_aniversario(self, ano_referencia, mes_referencia):
        data_proximo_aniversario = datetime(ano_referencia, self.data_nascimento.month, self.data_nascimento.day)
        
        if data_proximo_aniversario < datetime(ano_referencia, mes_referencia, 1):
            
            data_proximo_aniversario = datetime(ano_referencia + 1, self.data_nascimento.month, self.data_nascimento.day)
        
        dias_faltantes = (data_proximo_aniversario - datetime(ano_referencia, mes_referencia, 1)).days
        return data_proximo_aniversario, dias_faltantes

    def obter_nome_dia_semana(self, data):
        dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        return dias_semana[data.weekday()]