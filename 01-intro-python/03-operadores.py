# Operadores aritiméticos
# +, -, *, /, %, **

nota1 = 3
nota2 = 5.3

media = (nota1 + nota2)/2

# 2 elevado ao quadrado
potencia = 2 ** 2

# 2 elevado ao cubo
potencia = 2 ** 3


# Operadores de atribuição
# =, +=, -=, ++, ...
idade = 20

# idade = idade + 10
idade += 10


# Operadores lógicos
# and, or, not

resultado = True or False
print(type(resultado))
print(resultado)

# and
# 1 1 = 1
# 1 0 = 0
# 0 1 = 0
# 0 0 = 0

# or
# 1 1 = 1
# 1 0 = 1
# 0 1 = 1
# 0 0 = 0

# Operadores de comparação
# ==, !=, >, <, >=, <=

idade = 17
maior_de_idade = idade >= 18

if maior_de_idade:
    print('Maior de idade')
else:
    print('Menor de idade')

# operador is
# os valores do objeto e se ocupam o mesmo espaço de memória
a = [1,2,3]
b = [1,2,3]

# False. Não ocupam o mesmo espaço na memória
print(a is b)

z =[1,2,3]
x = z
# True ocupam o mesmo espaço de memoria
print(z is x)


# Operador in e not in
# verificar se um objeto está ou não dentro de uma sequência (str, set, tuple, dict, list, ...)

# True
print('y' in 'python')
print('Maria' not in ['João', 'Ana'])

#False
print('Maria' in ['João', 'Ana'])
