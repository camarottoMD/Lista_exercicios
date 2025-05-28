nome = []
i = 0
while i < 5:
    nome.append(input("Insira um nome: "))
    i += 1
    for y in range(5):
        print(f'{nome[y]} \n')
        