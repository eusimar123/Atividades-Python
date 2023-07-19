# 5. Escreva um programa que pergunte o valor inicial de uma dívida, o juro mensal.
# Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, 
#o total pago e o total de juros pago.
#valor_inicial = float(input("Digite o valor inicial da dívida: "))
#juro_mensal = float(input("Digite o juro mensal (em decimal): "))
#valor_pago_mensal = float(input("Digite o valor mensal a ser pago: "))
#meses = 0
#total_pago = 0
#total_juros = 0
#while valor_inicial > 0:
#    juros = valor_inicial * juro_mensal
#    valor_inicial += juros
#    valor_inicial -= valor_pago_mensal
#    meses += 1
 #   total_pago += valor_pago_mensal
# #   total_juros += juros
  #  if valor_inicial < 0:
  #      valor_inicial = 0
#print(f"Número de meses para pagar a dívida: {meses}")
#print(f"Total pago: R${total_pago:.2f}")
#print(f"Total de juros pago: R${total_juros:.2f}")


# Augusto, não conseguir colocar pra exibir as linhas de códicos que começa com o print

divida = float(input('Digite o valor de sua dívida: '))
taxa = float(input('Insira o valor da taxa de juros mensal: '))
valor_parcela = float(input('Insira o valor da parcela a ser paga: '))
mes = 1
if valor_parcela < divida*taxa/100:
    print('Você nunca pagará a dívida')
else:
    saldo_devedor = divida
    juros_pagos = 0
    while saldo_devedor > valor_parcela:
        juros = saldo_devedor*taxa/100
        saldo_devedor = saldo_devedor + juros - valor_parcela
        juros_pagos = juros_pagos + juros
        print(f'Mês {mes} // Saldo devedor R${saldo_devedor:6.2f}')
        mes = mes + 1
    juros = saldo_devedor*taxa/100
    saldo_devedor = saldo_devedor + juros
    juros_pagos = juros + juros_pagos
    if valor_parcela > saldo_devedor:
        saldo_devedor = 0
        print(f'Mês {mes} // Saldo devedor R${saldo_devedor:6.2f}')
    print(f'Os juros pagos foram de R$ {juros_pagos:6.2f}')
