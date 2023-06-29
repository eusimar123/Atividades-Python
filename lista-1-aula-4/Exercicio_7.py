# 7. Suponha que determinado usuário possua 2 logins em uma rede corporativa.
# Login 1
# usuario: jardim
# senha: flores1206
# Login 2
# usuario: cordeiro
# senha la1506
# Escreva um programa que valide o acesso do usuário na rede. Caso o par usuário e senha estejam corretos, o programa deve imprimir a mensagem: "Seja bem vindo!". Caso contrário, "Usuário e senha não conferem".
logins = {
"jardim": "flores1206",
"cordeiro": "la1506"
}
usuario = input(" Digite o usuário: ")
senha = input(" Digite a senha: ")
if usuario in logins and logins[usuario] == senha:       
    print(" Seja bem-vindo! ")
else:
    print(" Usuário e senha não conferem. ")