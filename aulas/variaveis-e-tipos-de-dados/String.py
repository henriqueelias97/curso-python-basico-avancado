"""
Tipo String

Em python, um dado é considerado o tipo strindg vem sempre que:

- Estiver entre àspas simples -> 'uma string' , '234' , 'a', 'True , '42.3'
- Estiver entre àspas duplas -> "uma string", "234", "a", "True'
- Estiver entre àspas simples triples -> '''uma string''' , '''234''', '''a''', '''true''' , '''42.3'''
nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Ginas's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \n Jolie'
print(nome)
print(type(nome))

nome= ""Angelina
Jolie""
print(nome)
print(type(nome))
'
print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma em uma lista de strings

nome = 'Geek University'
print(nome[0:4]) #Slice de String

print(nome[5:15]) #Slice de String
"""
#['0','1','2','3','4','5','6','7','8','9','10',11,12,13,14}
#['G','e','e','k',' ','u','n','i','v','e','r','s','i','t','y']

nome = 'Geek University'

print(nome.split()[0])
print(nome.split()[1])

print(nome[::-1]) # Comece do primeiro elemento, vá até o último e depois inverta

print(nome.replace('e','i'))

nome1 = 'ana' #palindromo
print(nome1)

print(nome1[::-1])