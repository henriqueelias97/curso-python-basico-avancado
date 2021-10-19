"""
loop for

loop -> Estrutura de repetição.
For -> Uma dessas estruturas

C ou Java

for(int i = 0, i <limitador(10 por exemplo); i++){
   //execução do loop
}

Python

for item in interavel:
    //execução do loop



Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
  nome = 'Geek University'
- Lista
  lista = [1,3,5,7,9]
- Range
  números = range(1,10)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
números = range(1, 10)

# Temos que transformar em uma lista

#Exemplo de for 1
for letra in nome:
    print(letra)

#Para cada letra dentro deste iterável imprima esta letra.

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

#Exemplo de for 3 (Iterando sobre um range)
for numero in range (1, 10):
    print(numero)

range(valor_inicial, valor_final)

Obs: 0 valor final não inclusive (incluso)
1
2
3
4
5
6
7
8
9
10 - não

for numero in range (1, 10):
    print(numero)
"""
"""
Enumarate
 enumerate is useful for obtaining an indexed list:
 |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
 ou seja
  enumerate é uma forma de obter uma indexação de uma lista:
 |      (0, 'G'), (1, 'e'), (3, 'e'), (4, ''), (5, "U')
for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)
"""
#OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)
"""
for _, letra in enumarate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

nome = 'Geek University'
lista = [1,3,5,7,9]
numeros = range(1, 10) #temos que transformar em uma lista

Exemplo em Range 
qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
   print(f'Imprimindo {n}')
   
#Exemplo de utilização do for 

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
  num = int(input(f'informe o {n}/{qtd} valor: '))
  soma = soma + num
print(f'A soma é {soma}')

#COMO FAZER A OPERAÇÃO PULANDO UMA LINHA

nome = 'Geek University'
for letra in nome:
    print(nome, end='')
Exemplo
#Em Java
System.out.println(letra)
System.out.print(letra)

#Em C
printf("%c\n", letra)

Exemplo
nome = 'Geek University'
for letra in nome:
    print(letra, end='')
"""
#Resultado exemplo lopp em strings
nome = 'Geek'
for num in range(1,11):
  print(f'{nome * num}')
Geek
GeekGeek
GeekGeekGeek
GeekGeekGeekGeek
GeekGeekGeekGeekGeek
GeekGeekGeekGeekGeekGeek
GeekGeekGeekGeekGeekGeekGeek
GeekGeekGeekGeekGeekGeekGeekGeek
GeekGeekGeekGeekGeekGeekGeekGeekGeek
GeekGeekGeekGeekGeekGeekGeekGeekGeekGeek
...







