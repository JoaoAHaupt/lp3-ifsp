# 1. Números
# int
idade = 17

# float
altura = 1.81

# complex
# calculos com números complexos
numero_complexo = 1 + 2j

# 2. Booleano
verdade = True

falso = False

# 3. Sequências
# string, list, tuple, set, dict
nome = 'João Augusto Haupt Fonseca Oliveira'
frase = '''
Lepo
'''

# interpolação de str
nome = 'Lepo'
idade = 24

mensagem = f'{nome} é uma pessoa legal! Ela tem {idade} anos'

# char não existe
# usar string de tamanho 1
char = 'a'

# Como acessar um index especifico
nome = 'Silvio Santos'
print(nome[2])

# Métodos de str
print(nome.upper())
print(nome.capitalize())
print(nome.lower())
print(nome.isdigit())
print(nome.isdecimal())


# list
# lista de valores  
habilidades = ['java', 'react', 'python', 'javascript']
print(habilidades[2])

for i in habilidades:
    print(i)

# adicionar ao final da lista
habilidades.append('MySQL')

# adiciona em uma posição especifica
habilidades.insert(1, 'css')

# remover
habilidades.remove('css')

# tuple
# 'lista' de valores
# não pode ser alterada
raca_rpg = ('humano', 'elfo', 'judge holden')

def estatistica_notas(notas):
    maior = max(notas)
    menor = min(notas)
    media = sum(notas)/len(notas)
    return maior, menor, media

notas = [10, 3.5, 9.8]

estatistica = estatistica_notas(notas)
print(estatistica)

# desempacotar uma tupla
maior, menor, media = estatistica_notas(notas)
print(maior, menor, media)

# set
# conjunto de valoresnome
# não é indexado
# permite elementos duplicados
habilidades = {'java', 'python'}
habilidades.add('java') # não vai adicionar pois já existe
print(habilidades)

# dict 
# palavra -> definicao
# chave -> valor


pessoa = {
    'nome': 'Lepo',
    'idade':24,
    'altura':1.81
}

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['altura'])

# None
null = None
