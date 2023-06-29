# 6. Faça um programa que peça o nome e a idade do usuário e que ao final informe o ano de nascimento da pessoa.
# nome = (input(" Digite seu nome: "))
# idade = int (input(" Digite sua idade: "))
# ano_atual = 2023
# ano_nascimento = ano_atual - idade 
# print("Você nasceu no ano de", ano_nascimento)
import datetime
nome = input(" Digite seu nome: ")
idade = int(input(" Digite sua idade: "))
mes_aniversario = int(input(" Digite o mês de aniversário (em formato numérico): "))
ano_atual = datetime.date.today().year
ano_nascimento = ano_atual - idade
if datetime.date.today().month < mes_aniversario:
    ano_nascimento -= 1
print(" Você nasceu no ano de", ano_nascimento)