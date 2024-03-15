import re

# Ex01 - Escreva um programa em Python que solicita ao usuário um número inteiro e apresenta seu antecessor e sucessor.
num = int(input('Escreva um número inteiro: '))
print(f'SEU NUMERO:{num} ANTECESSOR: {num-1} SUCESSOR: {num+1}\n')

# Ex02 - Escreva um programa em Python que solicita ao usuário três números e apresenta a média aritmética dos números informados.
nums = input('Escreva três números separados por espaço: ').split(' ')
print(f'{(int(nums[0])+ int(nums[1])+ int(nums[2]) )/len(nums)}\n')

# Ex03 - Crie um programa em Python que recebe como entrada o valor de uma compra e apresenta como saída o valor final com desconto e o desconto aplicado com base nas seguintes regras:
preco = float(input('INSIRA UM PREÇO'))
if(preco >= 500):
    desconto = 15
elif(preco>= 100 and preco <=499.99):
    desconto = 10
elif(preco>= 10 and preco <=99.99):
    desconto = 5
else:
    desconto = 0

print(f'{desconto}% DE DESCONTO')
print(f'PREÇO FINAL: {preco-preco*(desconto/100)}\n')

# Ex04 - O código identificador de funcionários de uma empresa contém 7 caracteres, inicia com a sequência de caracteres BR, em seguida apresenta um número inteiro entre 0001 e 9999 e finaliza com o caractere X. 
cod = input('INSIRA UM CÓDIGO VÁLIDO: ')

def ex04(cod):
    if(len(cod) != 7):
        return'CÓDIGO INVÁLIDO\n'

    isBR = cod[0] == 'B' and cod[1] =='R'
    number = re.sub(r'[^0-9]', '', cod)

    isBeetwen = int (number) >= 1 and int(number) <= 9999

    isX = cod[6] == 'X'

    if( isBR and isX and isBeetwen):
        return'CÓDIGO VÁLIDO\n'
    else:
        return'CÓDIGO INVÁLIDO\n'

print(ex04(cod))

# Ex05 - Crie um programa em Python que solicita ao usuário um identificador e apresenta se o que foi informado é um valor válido ou inválido.
identificador = input('ESCREVA O NOME DE UMA VARIAVEL: ')
def Ex05(identificador):
    if (identificador[0].isnumeric() or '-' in identificador or ' ' in identificador or re.search(r'[^\w\s-]', identificador)):
        return 'IDENTIFICADOR ERRADO\n'
    else:
        return 'IDENTIFICADOR CORRETO\n'
print(Ex05(identificador))




# Ex06. Crie um programa em Python que recebe como entrada o comprimento, altura e a largura de um aquário e calcule as seguintes informações.
aquario = input('ENTRE COM O COMPRIMENTO, ALTURA E LARGURA DO SEU AQUARIO (separe por espaços): ').split(' ')
temp_ambiente = int (input('AGORA COLOQUE A TEMPERATURA AMBIETE: '))
temp_desejada = int (input('AGORA COLOQUE A TEMPERATURA AMBIETE: '))

def Ex06(comprimento,altura, largura, temperatura_ambiente, temperatura_desejada):
    volume = (comprimento * altura * largura) / 1000
    potencia = volume * 0.05 * (temperatura_desejada - temperatura_ambiente)
    filtragens_min = 2 * volume
    filtragens_max = 3 * volume

    result = (f'Volume do aquário: {volume}L\n'
              f'Potência do termostato: {potencia}\n'
              f'Mínimo de filtragens: {filtragens_min}L ou {filtragens_max}L por hora\n')
    
    return result

print(Ex06(int(aquario[0]), int(aquario[1]), int(aquario[2]), temp_ambiente, temp_desejada))


# Ex07. Utilizando as diretrizes de Índice de Massa Corporal (IMC) da Organização Mundial de Saúde (OMS), crie uma calculadora em Python que solicita ao usuário seu peso (Kg) e sua altura (m) e apresenta em qual classificação o indivíduo se encaixa.

peso = float(input("DIGITE SEU PESO (em Kg): "))
altura = float(input("DIGITE SUA ALTURA (em metros): "))

def Ex07(peso, altura):
    imc = peso / (altura * altura)
    tipo = ''

    if imc >= 40:
        tipo = 'Obesidade classe 3'
    elif 35 <= imc <= 39.9:
        tipo = 'Obesidade classe 2'
    elif 30 <= imc <= 34.9:
        tipo = 'Obesidade classe 1'
    elif 25 <= imc <= 29.9:
        tipo = 'Excesso de peso'
    elif 18.5 <= imc <= 24.9:
        tipo = 'Peso normal'
    else:
        tipo = 'Baixo peso'

    peso_ideal = 24.9 * (altura * altura)
    peso_necessario = peso_ideal - peso

    if imc < 18.5:
        mensagem = f'Você precisa ganhar {peso_necessario:.2f} kg para atingir o peso normal.'
    elif imc > 24.9:

        mensagem = f'Você precisa perder {peso_necessario:.2f} kg para atingir o peso normal.'
    else:
        mensagem = 'Você está dentro do peso normal.'

    return tipo, mensagem


classificacao, mensagem = Ex07(peso, altura)
print(f'Classificação: {classificacao}')
print(mensagem)
   
    


