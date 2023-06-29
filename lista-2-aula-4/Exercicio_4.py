# 4. Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores Mês a meês para os 24 primeiros meses. Imprima o total ganho com o juros no período.
# Obs.: A fórmula de cálculo de juros compostos e que se aplica ao caso da questão é:
#  M = C*(1+i/100)*t
# No qual C é o valor inicial; i é a taxa de juros e t é o tempo em acordo com a taxa.
deposito_inicial = float(input(" Digite o valor do depósito inicial: "))
taxa_juros = float(input(" Digite a taxa de juros (%): "))
total_ganho_juros = 0
for mes in range(1, 25):
    juros_mes = deposito_inicial * (taxa_juros / 100)
    deposito_inicial += juros_mes
    total_ganho_juros += juros_mes
    print(f" Mês {mes}: Valor com juros: R$ {deposito_inicial:.2f}")
print(f" Total ganho com juros no período: R$ {total_ganho_juros:.2f}")



