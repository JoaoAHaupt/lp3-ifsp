# Ex01 - Escreva um programa em Python que solicita ao usuário um número inteiro e apresenta seu antecessor e sucessor.
num = int(input('Escreva um número inteiro: '))
print(f'SEU NUMERO:{num} ANTECESSOR: {num-1} SUCESSOR: {num+1}')

# Ex02 - Escreva um programa em Python que solicita ao usuário três números e apresenta a média aritmética dos números informados.
nums = input('Escreva três números separados por espaço: ').split(' ')
print(f'{(int(nums[0])+ int(nums[1])+ int(nums[2]) )/len(nums)}')

# Ex03 - Crie um programa em Python que recebe como entrada o valor de uma compra e apresenta como saída o valor final com desconto e o desconto aplicado com base nas seguintes regras:
preco = float(input('INSIRA '))
if(preco >= 500):
    desconto = 15
elif(preco>= 100 and preco <=499.99):
    desconto = 10
elif(preco>= 10 and preco <=99.99):
    desconto = 5
else:
    desconto = 0

print(f'{desconto}% DE DESCONTO')
print(f'PREÇO FINAL: {preco-preco*(desconto/100)}')

# Ex04 - O código identificador de funcionários de uma empresa contém 7 caracteres, inicia com a sequência de caracteres BR, em seguida apresenta um número inteiro entre 0001 e 9999 e finaliza com o caractere X. 
cod = input()

def ex04(cod):
    if(len(cod) != 7):
        return'CÓDIGO INVÁLIDO'

    isBR = cod[0] == 'B' and cod[1] =='R'

    number = cod.replace(cod[0], '')
    number = number.replace(cod[1], '')
    number = number.replace(cod[6], '')

    isBeetwen = int (number) >= 1 and int(number) <= 9999

    isX = cod[6] == 'X'

    if( isBR and isX and isBeetwen):
        return'CÓDIGO VÁLIDO'
    else:
        return'CÓDIGO INVÁLIDO'

print(ex04(cod))

# Ex06. Crie um programa em Python que recebe como entrada o comprimento, altura e a largura de um aquário e calcule as seguintes informações.
def aquario(comp, alt, largura):
    volume = (comp * alt * largura) / 1000