"""
Tipo Booleano

Algebra Booleana, criada por Geoge Boola

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

Obs: Sempre com inicial maiúscula

Errado:

true, false

Certo:

True, False
"""
ativo = False

print(ativo)

"""
Operações Básicas 
"""

# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso
se for falso o resultado será verdadeiro. Ou seja, sempre ao contrário.
"""
print (not ativo)

logado = False

# ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro 

True or True -> True
True or False -> True
False or True -> True
False or False -> False

"""
print(ativo or logado)

#E (and)
"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos os 
valores devem ser verdadeiros.

True and True -> True
True and Fase -> False 
False and True -> False 
False and False -> True
"""
