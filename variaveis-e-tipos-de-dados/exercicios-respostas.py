
# Exercicio 1

print('Leitura de um número inteiro e impressão do mesmo')
valor = int(input('Digite um número inteiro'))
print(valor)

# Exercicio 2

print('Leitura de um número real e impressão do mesmo')
valor = float(input('Digite um número real'))
print(valor)

# Exercicio 3

print('leitura de um 3 valores e resultado de sua soma')
valor1 =int(input('Digite o primeiro valor'))
valor2 =int(input('Digite o segundo valor'))
valor3 =int(input('Digite o terceiro valor'))

Valor = valor1 + valor2 + valor3
print(f'A soma é {Valor}')

# Exercicio 4

print('leitura de um número real e resultado do quadrado deste valor')
valor = float(input('Digite um número real'))
print(valor*valor)

# Exercicio 5

print('leitura de um número real e impressão de sua quinta parte')
valor = float(input('Digite um número Real'))
print (valor/5)

# Exercicio 6

print('Conversão de Celcius para Fahrenheit')
C = float(input('Qual a temperatura?'))
F = (C*(9.0/5.0)+32.0)
print(f'A temperatura convertida é {F}')

# Exercicio 7

print('Conversão de Fahrenheit para Celcius')
F = float(input('Qual a temperatura?'))
C = 5.0*(F -32.0)/9.0
print(f'A temperatura convertida é {C}')

# Exercicio 8

print('Conversão de Celcius par Kelvins')
K = float(input('Qual a temperatura?'))
C = (K - 273.15)
print('A temperatura em Kelvins é {C}')

# Exercicio 28

print('Cálculo da soma dos quadrados dos valores')
valor1 =int(input('Digite o primeiro valor'))
valor2 =int(input('Digite o segundo valor'))
valor3 =int(input('Digite o terceiro valor'))

Valor =((valor1**2)+(valor2**2)+(valor3**2))
print(f'A soma é {Valor}')

# Exercicio 29

print('Cálculo de media artimética')
valor1 =int(input('Digite o primeiro valor'))
valor2 =int(input('Digite o segundo valor'))
valor3 =int(input('Digite o terceiro valor'))

Valor =((valor1+valor2+valor3)/3)
print(f'A média é {Valor}')

# Exercicio 31

print('Impria o sucessor e o sucessor de um valor X')
Valor1 =int(input('Digite o primeiro valor'))
s = (Valor1 + 1)
m = (Valor1 -1)
print(f'O sucessor é {s} e o antecessor é {m}')

# Exercicio 32

print('Imprima a soma do sucessor do seu triplo e o antecessor do dobro de um valor X')
Valor1 =int(input('Digite o primeiro valor'))
s = (Valor1 * 3)+1
m = (Valor1*2)-1
print(f'O sucessor é {s} e o antecessor é {m}')

# Exercicio 34

print('Aréa do círculo')
r = float(input('Qual o valor do raio?'))
a = 3.141592 * (r ** 2)
print(f'A área é de {a}')

# Exercicio 35

print('Cálculo de hipotenusa')
import math
r = float(input('Qual o valor do cateto aposto?'))
b = float(input('Qual o valor do cateto adjacente?'))
Y = (r**2) + (b**2)
g = math.sqrt(Y)
print(f'A hipotenusa é {g}')
