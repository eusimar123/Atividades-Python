# 1. Faça um programa que escreva a contagem regressiva do lançamento de um foguete. O programa deve imprimir na tela a sequência regressiva de 10 até 0 e 'Fogo!'.
import time
for i in range(10, 0, -1):
     print(i)
     time.sleep(1)  
print("Fogo!")