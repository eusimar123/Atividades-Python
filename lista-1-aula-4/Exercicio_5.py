# 5. Escreva um programa que leia dois números e que pergunte qual operação o usuário deseja realizar. Esse programa deve aceitar como respostas a soma(+), a subtração(-), a multiplicação (*) e a divisão (/). Ao final, o programa deve exibir o resultado da operação escolhida.
numero1 = float(input(" Digite o primeiro número: "))
numero2 = float(input(" Digite o segundo número: "))
operacao = input(" Qual a operação desejada (+, -, *, /): ")
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
else:
    print(" Operação inválida. Por favor, escolha uma das opções válidas: +, -, *, / ")
    exit()
print(" O resultado da operação é:", resultado)