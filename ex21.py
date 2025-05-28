numeros = []

for num in range(10):
    numeros.append(int(input("Insira um número: ")))
    for num in numeros:
        if num % 2 == 0:
            numeros.remove(num)
print(numeros)

pares = [x for x in lista if x % 2 == 0]