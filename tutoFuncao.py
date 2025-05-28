""" 
Funcao em python e separada em tres partes: nome, parâmetros e corpo
argumento = valor de fato passado para funcao (numero real como: 10, 2.9)
parametro = variavel para definir uma funcao (numero imaginario como: n)

num = input(int("Digite um numero")) -> recebe um valor e retorna valor, retorna um print e recebe um input > int e funcao, oque o usuario coloca e retornado como uma funcao int
num = num+3
print(num) -> num e argumento
"""

def multiplicar_por_7(n): #variavel necessaria para o funcionamento da funcao, ele e o parametro
    res = 7 * n  
    return res

#FUNCAO QUE TEM MAIS DE UM PARAMETRO
def media_simples(a, b):
    return (a+b)/2 #-> escopo -> so existem aqui dentro

r = multiplicar_por_7(10) #-> valor utilizado na funcao, isso e um argumento
print(f'Resultado e: {r}')

print(media_simples(10,8))

res = multiplicar_por_7(6) # isso nao tem nada haver com o 'res' que esta dentro do escopo da funcao multiplica_por_7
print(res)

'''
a=8
b=32
media_simples(b,a) 

Isso tambem e diferente do que esta dentro do escopo na funcao
na funcao, isso vai ser interpretado de acordo com a ORDEM, assim fazendo com que a = 32 e b = 8
'''

'''def pedir_algo():
    print("Isso e uma funcao sem parametro")
    
pedir_algo()'''

listaLados =[]

for i in range(1,4):
    l[i]= input((f"Insira o tamanho do lado {i}: "))
    listaLados.append(l[i])
    for lado in range(listaLados):
            variavel[i] = listaLados[lado]
print(l[i])
#def tarefa(l1, l2, l3):

#DUVIDA, COMO FAZER UMA FUNCAO QUE A CADA LOOP DE REPETICAO, CRIA UMA NOVA VARIAVEL