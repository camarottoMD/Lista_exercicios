lista = []

for i in range(5):
    lista.append(int(input('Insira um número até se acumular cinco número: ')))
    
for j in range(len(lista)):
    if lista[j] > 10:
        print(f'O número {lista[i]} é maior que 10')
    else:
        print(f'O número {lista[i]} não é maior que 10')
