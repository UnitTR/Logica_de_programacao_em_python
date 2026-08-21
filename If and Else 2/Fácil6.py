# Elabore um programa que receba a quantidade de faltas de um aluno e informe se ele foi reprovado por faltas. Considere que ele não pode ter mais de 25% de faltas da quantidade de horas no curso. (Horas no curso = 1200).

faltas = int(input("Informe a sua quantidade de faltas:    "))

valor_faltas = faltas * 4 # Cada aulas tem uma duração de 4h!
limite = (1200 * 0.25) 

if (valor_faltas < limite):
    print("Você está aprovado!")
else:
    print("Você superou o limite de 25% de faltas, você está reprovado!")