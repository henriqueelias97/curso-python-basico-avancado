"""
Tuplas (tuple)

Tuplas são bastante parecidas ccom listas.

Existem basicamente duas difernças básicas:

1 - As tuplas são representadas por parenteses ()

2 - As tuplas são imutáveis, ou seja ao se criar uma tupla ela não pode ser alterada. Toda operação
em uma tupla gera uma nova tupla.

# Cuidado 1 - As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# Cuidado 2 - Tuplas com 1 elemento

tupla3 =(4) # Isso não é uma tupla!
print(tupla3)

print(type(tupla3))

tupla4 = (4,) #Isso é uma tupla!
print(tupla4)

print(type(tupla4))

tupla5 = 4,
print(tupla5)

print(type(tupla5))
#Conclusão: Tuplas são definidas pela virgula e não pelo uso do parênteses.

4 -> Não é tupla
4,-> É tupla
(4,) -> é tupla

# Podemos gerar uma tupla dinamicamente com range( inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Geek Univerisity', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

#OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos para desempacotarmos

#Métodos para: Adição, remoção  de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.

# Soma, valor máximo, valor minimo e tamanho

# *Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6,)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

#Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) #Tupla são imutáveis

tupla3 = tupla1 + tupla2

print(tupla1)
print(tupla2)
print(tupla3)

tupla1 = tupla1+ tupla2 # Tuplas são imutáveis, mas podemos sobrescrever seus valores.
print(tupla1)

#Verificação se determinado elemento está conntido na tupla

tupla = (1, 2, 3)

print(33 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3)
for n in tupla:
    print(n)

for i, valor in enumerate(tupla):
    print(i, valor)

# Contando elementos dentro de uma tupla

tupla =('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('b'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

# Não faz sentido haver modificações em operadores definidos

print(meses)

# O acesso a elementos de uma tupla é bem semelhante a de uma lista

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'NOvembro', 'Dezembro')
print(meses[5])

#Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual indice um elemento está na tupla

print(meses.index('Junho'))

# Não existindo o elemento temos o retorno de um (ValueError)
# Slicing

# tupla[inicio:fim:passo]

print(meses[5:9])

# Por que utilizar tuplas?

# Tuplas são mais rapidas do que listas.
# tuplas deixam seu código seguro

# Isso porque trabalhar com elementos imutáveis traz segurança para o código

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla # Na tupla não temos o problema de Shallow Copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)
"""




