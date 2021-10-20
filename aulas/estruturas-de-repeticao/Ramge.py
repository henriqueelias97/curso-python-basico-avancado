"""
Ranges

- Precisamos conhecer o loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numericas, não de forma aleatória, mas
sim de maneira especificada

Forma gerais:

range(valor_de_parada)

obs: valor_de_parada não inclusive (inicia em 0, e passo de 1 em 1)
#forma 1
for num in range(11):
    print(num)
#Forma 2

range(valor_de_inicio, valor_de_parada)
obs: valor_de_parada não inclusive (inicia em 0, e passo de 1 em 1)

for num in range(1,11):
    print(num)

#Forma 3

range(valor_de_inicio, valor_de_parada, passo)]

obs: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário)

Exemplo 3
for num in range(1, 10, 2):
    print(num)
1
3
5
7
9

Forma 4 (3 inversa)

range(valor_de_inicio, valor_de_parada, passo)

obs: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário)

for num in range(10, 0, -1):
    print(num)
10
9
8
7
6
5
4
3
2
1

"""
[print(x) for x in range(15, 0, -3)]

'''Método clean code outra operação de range'''