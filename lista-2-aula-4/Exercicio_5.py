# 5. Escreva um programa que pergunte o valor inicial de uma dívida, o juro mensal.
# Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, 
#o total pago e o total de juros pago.
valor_inicial = float(input("Digite o valor inicial da dívida: "))
juro_mensal = float(input("Digite o juro mensal (em decimal): "))
valor_pago_mensal = float(input("Digite o valor mensal a ser pago: "))
meses = 0
total_pago = 0
total_juros = 0
while valor_inicial > 0:
    juros = valor_inicial * juro_mensal
    valor_inicial += juros
    valor_inicial -= valor_pago_mensal
    meses += 1
    total_pago += valor_pago_mensal
    total_juros += juros
    if valor_inicial < 0:
        valor_inicial = 0
print(f"Número de meses para pagar a dívida: {meses}")
print(f"Total pago: R${total_pago:.2f}")
print(f"Total de juros pago: R${total_juros:.2f}")


# Augusto, não conseguir colocar pra exibir as linhas de códicos que começa com o print
