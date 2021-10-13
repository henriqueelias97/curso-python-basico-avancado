#Exercicio 1

print ('Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números'
'maiores que zero')

for num in range(3, 18, +3):
    print(num)

#Exercicio 5

print('Faça um programa que peça ao usuário para digitar 10 valores e some-os')

soma = cont = mum = 0
while cont !=10:
   num = int(input('Digite um número: '))
   soma += num
   cont += 1
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))

#Exercicio 10

print('Faça um programa que calcule e mostre a soma dos 50 primeiros números pares')
cont = soma = 0

for num in range(1, 200):
    if num%2 == 0 and cont <= 50:
        soma = num + soma
        print(num)
        cont += 1
    if cont == 50:
        print(soma)
        break

#Exercicio 15

print ('Faça um programa que leia um número inteiro positivo impar N e imprima todos os números'
       'impares de 1 até N em ordem crescente')

valor = int(input('Escreva um número inteiro positivo'))

print()
if (valor > 0) and (valor % 2 == 1):
    print(f'Todos os números de 1 até {valor} em ordem crescente')
    for i in range (1, valor):
        if i % 2 == 1:
            print(i)
else:
    print('Este valor não é impar')

#Exercicio 20

print('Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá'
      'ser informado o número de dados lidos e números de valores pares. O processo termina'
      'quando for digitado o valor 1000')

num = 0
cont1 = 0
cont2 = 0

while num != 1000:
"""
#!= É DIFERNETE DE
"""
    num = int(input("Digite um número: "))

    if (num > 0) and (num % 2 == 0) or (num < 0) and (num %2 == -1):
        cont2 += 1

    cont1 += 1

print()
print(f'Número de dados lidos: {cont1}')
print(f'Os números de valores pares: {cont2}')

#Exercicio 25
print('Faça um programa que some todos os números naturais abaixo de 1000'
      'que são múltiplos de 3 e 5')

soma = 0

for i in range(1,1000):
    if (i % 3 == 0) and (i<1000) or (i % 5 == 0) and (i < 1000):
        soma += i
#for (i = 0, i > 10, i++) {
} i = index, operador indexável 

print(f"A soma de todos os números naturais abaixo de 1000 que são múltiplos de 3 e 5 é {soma}")

#Exercicio 26

print('Faça um algorito que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado')

num = int(input("Digite um número: "))

lista = [11, 13, 17]

print()
print(f'O primeiro múltiplo de 11, 13 ou 17 de {num} é:')
for x,y in enumerate(lista):
    print(num * y)

#Exercicio 32

from random import randint

print('Faça um programa que simula o lançamento de dois dados d1 e d2, n vezes e tem como saída o número '
      'de cada dado e a relação entre eles (>,<,=) de cada lançamento')

d1 = 0
d2 = 0

n = int(input("Digite o número de vezes que você deseja jogar os dois dados: "))

for i in range(n):
    d1 = randint(1, 6)
    d2 = randint(1, 6)

    print()
    print(f'Lançamento {i+1}:')

    if d1 > d2:
        print(f'Dado 1: {d1}')
        print(f'Dado 2: {d2}')
        print(f'Dado 1 > Dado 2')

    elif d1 < d2:
        print(f'Dado 1: {d1}')
        print(f'Dado 2: {d2}')
        print(f'Dado 1 < Dado 2')

    else:
        print(f'Dado 1: {d1}')
        print(f'Dado 2: {d2}')
        print(f'Dado 1 = Dado 2')
        
#Exercicio 34

print('Faça um programa que calcula o menor número dívisivel por cada um número de 1 a 20')

from math import gcd

def mmc(numeros):
    m = 1
    for n in numeros:
        m = m * n // gcd(m, n)
    return m

numeros = range(2, 21)
print(mmc(numeros))

#Exercicio 36

print('Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros'
      '100 números naturais eo quadrado da soma.')

qtd = 100

soma_quadrado = 0
quadrado_soma = 0

for i in range(1, qtd+1):
    soma_quadrado += i ** 2
    quadrado_soma += i

quadrado_soma = quadrado_soma ** 2

print(f'A soma dos quadrados dos {qtd} primeiros números naturais é {soma_quadrado}\n')
print(f'Quadrado da soma dos {qtd} primeiros números naturais é {quadrado_soma}\n')

print(f'A diferença entre a soma dos quadrados dos {qtd} primeiros números naturais'
      f' e o quadrado da soma é {quadrado_soma - soma_quadrado}')

