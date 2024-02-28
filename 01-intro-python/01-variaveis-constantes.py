for i in range(20):
    print('lepo' + str(i))


# Identificadores
# Letra, numeros e _
# \Não pode ser reservada: if, None, True, False, etc

nome = "lepo"
Nome = "Lepo"

# Variáveis 
# Tudo em minusculo
# Separador _
# snake_case
# Inferência de tipo. O proprio Python já associa o tipo

idade = 17 # int
nome = "João" # String

# Não existe constante no Pyhton
# Convenção: Nome em maisculo

PI = 3.14

# Comentarios de unica linha

'''
    comentarios de multiplas linhas 
'''

# docstring (comentario de documentção)
# documentar classes, objetos, funções, módulos, ...

def soma(num1, num2):
    '''
    Função que soma dois números
    :param num1: primeiro numero
    :param num2: segundo numero
    :return: soma dos nueros
    '''
    return num1 + num2

soma(1,1)