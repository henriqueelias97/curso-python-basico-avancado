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

"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3 , 1, 44, 42, 27]

lista2 = ["G", "e", "e", "k", " ", "U", "n", "i", "v", "e", "r", "s", "i", "t", "y" ]

lista3 = []

lista4 = list(range(11))

Lista5 = list("Geek University")

# Podemos facilmente checar se determinado valor esta contido na lista
num = 18
if num in lista4:
    print(f'Encontrei o número  {num}')
else:
    print(f'Não encontrei o número {num}')


