# Exercicio 1

print('Faça um program que receba dois núnmeros e mostre qual deles é o maior')
valor1 = int(input('Digite o primeiro valor'))
valor2 = int(input('Digite o segundo valor'))
if valor1 > valor2:
    print('O primeiro valor é maior')
elif valor2 > valor1:
    print("O segundo valor é maior")

#Exercicio 2

import math
print('Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número'
      'Se for negativo, mostre uma mensagem dizendo que o número é invalido')
valor1 = float(input('Digite o valor'))
if valor1 > 0:
    raiz = math.sqrt(valor1)
    print(raiz)
elif valor1 < 0:
    print('O valor é invalido')

#Exercicio 3

import math
print('Leia um número real.Se o número for positivo, imprima a raiz quadrada. Do contrário, imprima o número ao quadrado')
valor1 = float(input('Digite o valor'))
if valor1 > 0:
    raiz = math.sqrt(valor1)
    print(raiz)
elif valor1 < 0:
    print(valor1**2)

#Exercicio 4

import math
print('Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:'
      'O número digitado ao quadrado'
      'a raiz quadrada do número digitado')
valor1= float(input('Digite o valor desejado'))
if valor1 > 0:
    raiz = math.sqrt(valor1)
    print(f'A raiz quadrado do valor é {raiz}')
    quadrado = (valor1**2)
    print(f'O valor ao quadrado é {quadrado}')
elif valor1 < 0:
    print(valor1**2)

#Exercicio 5

print('Faça um programa que receba um número inteiro e verifique se este número é par ou impar')
valor1 = int(input('Digite um número inteiro'))
if valor1 == 0:
print('O valor é par')
else:
print('Número é impar')

#Exercicio 6

print('Escreva um programa que, dados dois números inteiro, mostre na tela o maior deles'
      'assim como a diferença existentes entre ambos')
valor1 = int(input('Digite o primeiro valor'))
valor2 = int(input('Digite o segundo valor'))
dif = valor1 - valor2
if valor1 > valor2:
        print(f'O maior valor é o primeiro, sua diferença é {dif}')
else:
        print(f'O valor dois é o maior,  sua diferença é {dif}')

#Exercicio 13

print('Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e'
      'a segunda prova tem peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno'
      'e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior'
      'a 60 pontos')
valor1 = float(input('Digite a primeira nota'))
valor2 = float(input('Digite a segunda nota'))
valor3 = float(input('Digite a terceira nota'))
final = ((valor1+valor2+valor3*2))
f1 = (final/3)
if f1 < 60:
    print(f'Você está reprovado, sua nota foi de {f1}')
else:
    print(f'Sua nota final é de {f1}')

#Exercicio 20

print('Dados três valores, A,B,C, verificar se eles podem ser valores dos lados de um triângulo e,'
      'se forem, se é um triângulo escaleno, quilátero ou isóscele, considerando os seguintes conceitos:'
      'Os comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados'
      'Chama-se equilátero o triângulo que tem três lados iguais'
      'Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais'
      'Recebe o nome de escaleno o triângulo que tem os três lados diferentes')

a = float(input('Digite o primeiro valor'))
b = float(input('Digite o segundo valor'))
c = float(input('Digite o terceiro valor'))

if (a + b < c) or (a + c < b) or (b + c < a):
    print('Nao é um triangulo')
elif (a == b) and (a == c):
    print('O triângulo é Equilatero')
elif (a == b) or (a == c) or (b == c):
    print('O triângulo é Isósceles')
else:
    print('O triângulo é Escaleno')

#Exercicio 21

print('Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. Escreva uma mensagem '
      'de erro se a opção for inválida')

from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opcão = 0
while opcão != 5:
    print(''' 
    [1] Somar
    [2] Diferença entre 2 números
    [3] Produto entre 2 números
    [4] Divisão entre 2 números
    [5] Sair do programa
    ''')
    opção = int(input('Qual a sua opção? '))
    if opção == 1:
           soma = n1 + n2
           print('a soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
           dif = n1 - n2
           print('a diferença entre {} e {} é {}'.format(n1, n2, dif))
    elif opção == 3:
           multi = n1 * n2
           print('o produto entre {} e {} é {}'.format(n1, n2, multi))
    elif opção == 4:
           divI = n1 / n2
           print('o produto entre {} e {} é {}'.format(n1, n2, divI))
    elif opção == 5:
           print('Finalizando')
    else:
            print('Opção inválida. Tente novamente.')
    print('Fim do prograna!')
    sleep(2)

#Exercicio 36
print('Escreva um programa que, dado o valor da vena, imprima a comissão que deverá ser paga ao vendedor.'
      'Para calcular a comissão, considere a tabela abaixo')

n1 = float(input('Qual foi o valor de venda do vendedor: '))

if n1 >= 100000:
    soma1 = 700 + n1 * 0.16
    print(f'a comissão do vendedor é {soma1}')
elif n1 > 100000 and n1 >= 80000:
    soma2 = 650 + n1 * 0.14
    print(f'a comissão do vendedor é {soma2}')
elif n1 < 80000 and n1 >= 60000:
    soma3 = 600 + n1 * 0.14
    print(f'a comissão do vendedor é {soma3}')
elif n1 < 60000 and n1 >= 40000:
    soma4 = 550 + n1 * 0.14
    print(f'a comissão do vendedor é {soma4}')
elif n1 < 40000 and n1 >= 20000:
    soma5 = 500 + n1 * 0.14
    print(f'a comissão do vendedor é {soma5}')
else:
    soma6 = n1 * 0.14 + 400
    print(f'a comissão do vendedor é {soma6}')

