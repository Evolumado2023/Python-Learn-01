nome = input("Digite o seu nome: ")
idade = input("digite a sua idade: ")
profissao = input("Qual a sua profissão?: ")

cadastro = nome, idade, profissao

print("Seu nome é ", nome, ", você tem ", idade, " anos, e sua profissão é ", profissao)

print (cadastro)

if len(cadastro == 0):
    print("A lista de dados em cadastro está vazia")




