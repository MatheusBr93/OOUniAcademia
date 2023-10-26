from AlunoEnsinoMedio import AlunoEnsinoMedio
from AlunoGraduacao import AlunoGraduacao
from Professor import Professor



print("*********************************************")
medio1 = AlunoEnsinoMedio()
medio1.setNome("Vitin")
medio1.setMatricula(90900046406)
medio1.setNota(6)
medio1.setNota(5)
medio1.setNota(4)
medio1.media()
print(medio1)
print("*********************************************")
graduacao1 = AlunoGraduacao()
graduacao1.setNome("Vitão")
graduacao1.setMatricula(999999999)
graduacao1.setNota(6)
graduacao1.setNota(8)
graduacao1.setNota(7)
graduacao1.media()
print(graduacao1)

print("*********************************************")
professor1 = Professor()
professor1.setNome("Marcos Miguel")
professor1.setTitulacao("Mestre")
print(professor1)


















