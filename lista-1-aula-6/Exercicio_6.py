# 6. Escreva um programa que receba um texto e uma palavra, então verifique se a palavra está no texto..
def verificar_palavra(texto, palavra):
    palavras_texto = texto.split()  # Dividir o texto em uma lista de palavras
    if palavra in palavras_texto:
        return True
    else:
        return False
texto = input(" Digite o texto: ")
palavra = input(" Digite a palavra a ser verificada: ")
if verificar_palavra(texto, palavra):
    print(" A palavra", palavra, "está presente no texto. ")
else:
    print(" A palavra", palavra, "não está presente no texto. ")