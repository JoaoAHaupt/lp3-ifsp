# Função
# Modularizar o programa
# manutentabilidade

# só pode acessar hora se estiver entre 8h e 18h


# entrada = hora_atual
# saída se esta dentro ou não do horário atual

hora = 12

def dentro_horario_comercial(hora_atual):
    return hora_atual >= 8 and hora_atual <= 18

dentro_horario_comercial(hora)

# Declaração
# def nome_funcao():
#     corpo da funcao

# funcao sem retorno

def diga_ola(nome):
    print(f'Olá {nome}!')
# chamada
diga_ola('Marcos')

# funcao com retorno
# side effect - efeito colateral
def montar_frase(nome):
    return f'Olá {nome}'

nome = 'MarcosLEpo'
print(montar_frase(nome))


# Parâmetro e Argumentos
# Parâmentro referências que podem ser acessadas dentro da função
# Argumento são os valores passados para os parâmetros

def somar(num1 , num2):
    return num1 + num2

somar(10.0, 23.2)

# Escopo de variáveis 
# Variável local

def calcular_media(nota1, nota2, nota3):
    media = (nota1+ nota2+ nota3)/3
    return media


# Variável Global
total = 0.0

def soma(n1,n2,n3):
    global total
    total = n1+ n2 +n3
    return total

print(total)
soma(1,2,3)
print(total)

# Parâmetros com valor default

def boas_vindas(nome , mensagem='Bom dia'):
    return f"{mensagem}, {nome}"

print(boas_vindas('Marcos'))
print(boas_vindas('Lepo'))

# Argumentos nomeados
print(boas_vindas(nome='Maria'))

# Docstring
# comentário na documentação

def somar(n1,n2):
    '''
    Função que soma dois numeros
    '''
    return n1+n2