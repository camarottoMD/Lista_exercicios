lista = ['matheus', 'matheus', 2, 3, 4, 2]
def retornaSet(lista):
    #lista = ['matheus', 'matheus', 2, 3, 4, 2] -> com isso não precisa de parametro na função
    conjunto = list(set(lista))
    print(conjunto)

retornaSet(lista)