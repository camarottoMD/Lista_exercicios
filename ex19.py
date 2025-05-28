nomes = []

while True:
    nome = (input("Insira um nome: "))
    nomes.append(nome)

    if nome == 'sair':
        break
    
nomes.pop(-1)
print(nomes)
    