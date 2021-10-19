"""
Escopo de variavéis

Dois casos de escopos:

1 Váriaveis Globais:
   - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o program

2 - Variáveis locais;
  -  Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
  está liomitado ao bloco que foi decladara.

Para declarar variáveis em Python fazemos:

Nome_da_variável = valor_da_variável

python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é o inferido ao atribuido o valor à mesma.

Exemplo em C:
int número = 42

Exemplo em Java:
int numero = 42
"""

numero = 42 # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

não_existo = 'oi'
print(não_existo)

numero = 42
novo = 0
if numero > 10:
   novo = numero + 10
   print(novo)

print(novo)