lista = []
pares = []

for i in range(1,11):
    lista.append(i)

for p in lista:
    if p % 2 == 0:
        pares.append(p)

print(pares)