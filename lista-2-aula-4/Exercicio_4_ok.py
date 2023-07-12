deposito = float(input('Insira o valor a ser depositado:'))
taxa = float(input('Insira o valor da taxa de juros: '))
tempo = 1
while tempo <= 24:
    mont = deposito*(1+taxa/100)**tempo
    print('Mês', tempo, 'O valor é R${:.2f}'.format(mont))
    tempo = tempo + 1
juros = mont - deposito
print(round(juros,2))


# copiei da sua correção só pra comparar com a que eu fiz, porque
#  eu utilizei o for em vez do while, mas pode desconsiderar ESSA 
# questão e deixar a que eu fiz valendo a nota