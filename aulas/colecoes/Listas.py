"""
Listas

Listas em python funcionam como vetores ou matrizes -

Entendido como arrays em outras linguagens, porém com a diferença de serem dinâmicos e
também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dados fixo:
     ou seja, nessas linguagens se você criar um array do tipo in e com tamanho 5
     será sempre do tipoi INTEIRO e poderá ter SEMPRE no máximo 5 valores.

Já em Python:

- Dinâmicos: Não possui tamanho fixo, ou seja podemos criar lista e simplesmente ir adicionando
  elementos;
  Isso não quer dizwr que lista é infinita, uma vez que existe limitação de memória.

- Qualquer tipo de dado: Não possuem tipo de dado fixo: Ou seja, podemos colocar qualquer tipo de dado:

As listas de em Python são representadas por conchetes []:

# Podemos facilmente checar se determinado valor esta contido na lista
num = 18
if num in lista4:
    print(f'Encontrei o número  {num}')
else:
    print(f'Não encontrei o número {num}')

# podemos facilmente ordenar a uma lista
# Comando SORT() serve para ordenamento de listas
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências e um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas

"""
# Para adicionar elementos em listas, utilizamos a função append, função APPEND recebe apenas UM argumento
"""
print(lista1)
lista1.append(42)
print(lista1)

# o que é possivel de ser feito, coloca a lista como um único elemento

lista1.append([8, 3, 1])
print(lista1)

if 22 in lista1:
    print('encontrei a lista')
else:
    print('Não encontrei a lista')

#outra operaçãp

lista1.extend([123, 44, 67])
print(lista1)

#extend faz da mesma forma que append, porém podendo adicionar mais de um elemento sem a necessídade de ser uma variável
#única
#extend só aceita iteráveis como ex: Listas, Strings,

# podemos inserir um novo elemento na lista informando a posição do indice
#OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita. 

lista1.insert(2, 'Novo Valor')
print(lista1)

#Podemos facilmente unir duas listas.

# lista6 = lista1 + lista2
# print(lista6)

lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista utilizando o reverse

forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# outra forma de realizar isso

forma 2 
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

#Para saber o tamanho da lista, ou seja quantos elementos esta lista contém,  utilizamos len de length 

print(len(lista1))

# Podemos remover facilmente o último elemento de uma lista
# Não somente o remote o último elemento mas tambem o retorna

print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice 
lista5.pop(2)
print(lista5)

# Podemos remover um elemento pelo indice
# Os elementos a direita deste indice serão deslocados para a esquerda
# Se não houver elemento no indice informado, haverá um erro

lista5.pop(2)
print(lista5)

#Podemos remover todos os elementos (zerar)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [ 1, 2, 3]
print(nova)
nova = nova * 3 
print(nova)

# Podemos facilmente converter uma string para uma lista

# Exemplo 1

curso = 'Programação em python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# Obs: Por padrão, o split separa os elementos da lista pelo espaço entre elas

# Exemplo

curso = 'Programação,em,python,essencial'
print(curso)
curso = curso.split(',')
print(curso)

#Abaixo estamos falando: Receba a lista6, porém colocando espaço entre cada elemento e transforme esta em string
curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso) 

# Podemos realmente colocar qualquer tipo de dado em uma lista, incluseive misturando estes dados.

lista6 = [1, 2, 34, True, 'geek', 'd', [1, 2, 3], 45345345345]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 - Utilizando for 

soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# Convertendo uma lista em String

lista6 =['Programação', 'em', 'Python', 'Essencial']
print(lista6)

# Exemplo 2 = Utilizando while

carrinho = []
produto = ''

while produto !='sair':
    print("Adicione um produto na lista ou digite 'sair' para sair:")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
    
# Utilizando variáveis em listas, basicamente a mesma coisa.

numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de formas indexada

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

#Para entender melhor o indice negativo, pense na lista como um circulo onde
# o final de um elemento está ligado ao inicio da lista

cores = ['verde', 'amarelo', 'azul', 'branco']
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos 

# Encontrar o indice de um elemento na lista

numeros = [5, 6, 7, 8, 9, 10]

#em qual indice da lista está o valor 6?
print(numeros.index(6))

#Buscando dentro de um range, ou seja, qual indice começar a buscar

numeros = [5, 6, 7, 5, 8, 9, 10]

print(numeros.index(5, 1))

print(numeros.index(8, 3, 8)) # buscar o indice 8 entre 6 e 8

# Outros métodos não tão importantes, mas também úteis

# Revisão de slicing

# trabalhando com slice de lista com parâmetros inicio

#lista [Inicio, fim:passos]
# Range [Inicio;fim:passos]

lista = [1, 2, 3, 4]
print(lista[1:]) # iniciando no indice 1 e pegando todos os elementos restantes

# trabalhando com slide de lista com parãmetros 'fim'

print(lista[:2]) #começa em 0, pega até o índice 2-1

print(lista[:4]) # começa em 0, pega até o índice 3 -1

print(lista[1:3]) # começa em 1, pega até o 3-1

# trabalhando com slice de lista com parâmetros 'passo'

print(lista[1::2]) #começa em 1, vai até o final, de 2 em 2

print(lista[::2])  #começa em 0, vai até o final, de 2 em 2

# invertendo valores em uma lista

nomes = [ 'Geek', 'University']

nomes [0], nomes [1] = nomes [1], nomes [0]

print(nomes)

nomes = ['Geek', 'University']

nomes.reverse()
print(nomes)

# Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]
# Soma, Valor Máximo, Valor Minimo, Tamanho
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))


# Transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotando de listas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)


# Copiando uma lista para outra (shallow copy e deep copy)

# Forma 1 - deep copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy copiamos os dados da lista para uma nova, mas elas
# ficaram totalmente independtes, ou seja, modificando uma lista, não afeta a outra. Isso em python
# é chamado de deep copy

# Forma 2 - shallow copu

lista = [1, 2, 3]
print(lista)

nova = lista # copia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# apos realizar modificações em uma das listas, essa modificação se refletiu em amabas as listas.
# Isso em python é chamado em shallow copy
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3 , 1, 44, 42, 27]

lista2 = ["G", "e", "e", "k", " ", "U", "n", "i", "v", "e", "r", "s", "i", "t", "y" ]

lista3 = []

lista4 = list(range(11))

lista5 = list("Geek University")






