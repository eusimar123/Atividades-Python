# 4. Faça um programa que receba 3 notas de prova de um aluno, calcule a média e diga se ele foi aprovado ou reprovado. A média para aprovação é de pelo menos 6 (aprovado se média maior ou igual a 6).
nota1 = float (input(" Digite a nata da primeira prova: "))
nota2 = float (input(" Digite a nata da segunda prova : "))
nota3 = float (input(" Digite a nata da terceira prova: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 6:
    print(" O aluno foi aprovado! ")
else:
    print(" O aluno foi reprovado. ")
