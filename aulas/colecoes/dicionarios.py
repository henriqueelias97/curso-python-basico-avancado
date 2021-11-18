"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos
por mapas.

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}

print(type({}))

obs: Sobre Dicionários
    - Chaves e valor são separados por dois ponto 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado:
    - Podemos misturar tipos de dados;

# Criação de dicionários

# Forma 1 (mais comum)

países = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(países)
print(type(países))

#Forma 2 (menos comum)

paises1 = dict(br='Brasil', eua='estados unidos', py='paraguay')

print(paises1)
print(type(paises1))

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

#Acessandro elementos

#Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['py'])

#Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru'))

# Caso o GET não encontre o objeto com a chave informada será retornado o valor NONE e
não será gerado o KEYERROR

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

pais = paises.get('ru', 'Não encontrado')

if pais:
    print(f'Encontrei o pais {pais}')
else:
    print('não encontrei o pais')

#Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o pais {pais}')

# Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado, inclusive int, float, string, boolean, inclusive lista, tupla, dicionário, como
#chave de dicionário

#Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionário, pois as mesmas
#são imutáveis

localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.6895, 74.6917): 'Escritório em NY',
    (37.7649, 122.6917): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))


# Adicionar elementos em um dicionário

receita = {'jan' : 100, 'fev' : 120, 'mar' : 300}

print(receita)
print(type(receita))

#Forma 1

receita['abr'] = 350

print(receita)

#Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado) # receita.update({'mai':500})

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita ['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai' : 600})

print(receita)

# CONCLUSÃO 1 : A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# CONCLUSÃO 2 : Em dicionários, NÃO podemos ter chaves repetidas.


# Remover dados de um dicionário

# forma 1

receita = {'jan' : 100, 'fev' : 120, 'mar' : 300}

print(receita)

# Forma 1
# Mais comum

ret = receita.pop('mar')
print(ret)

#OBS1: Aqui precisamos sempre informar a chave, e caso não encontre o elemento, um KeyError é retornado.
#OB2: Ao removermos um objeto, o valor deste é sempre retornado.

# Forma 2

del receita['fev']

print(receita)

# Se a chave não existir será gerado um KeyError
# Não há retorno da remoção neste caso.

# Imagine que você tem um comercio eletronico, onde temos um carrinho de compras na qual adicionamos produtos
Carrinho de compras:
    Produto 1:
         - Nome;
         - QUantidade;
         - Preço;
    Produto 2:
         - Nome;
         - QUantidade;
         - Preço;
# 1 - Poderiamos utilizar uma lista

carrinho = []

produto1 = ['Playstation 4', 1, 230]
produto2 = ['God Of War 4',1, 150]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual o indice de cada informação do produto.

# 2 - poderiamos utilizar uma tupla? Si

produto1 = ('Playstation 4', 1, 230)
produto2 = ('God Of War 4',1, 150)

carrinho = (produto1, produto2)

print(carrinho)

# Opção 3 - Dicionário

carrinho = []

produto1 = {'nome': 'PLaystation 4' , 'quantidade': 1, 'preco': 230}
produto2 = {'nome': 'GOW 4' , 'quantidade': 1, 'preco': 200}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

#Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em produto
# podemos ter certeza da informação


# Métodos de dicionários

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionário (Zerar Dados)

d.clear()

print(d)

# Copiando um dicionário para outro

#Forma 1  #deep copy

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 # Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(type(d))

# Forma não usual de criação de dicionários

outro = {}. fromkeys('a', 'b')

print(outro)
print(type(outro))
"""

# Forma não usual de criação de dicionários

outro = {}. fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um interável e um valor
# Ele vai gerar para cada valor do iterável uma chave e irá atrabuir a esta chave um valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)