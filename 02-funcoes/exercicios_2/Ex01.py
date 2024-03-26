'''
    Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. 
    Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.
'''
import random
numberRandom = random.randint(1, 100)
print(numberRandom)
while True:
    num = int(input('Entre com um número aleatório ' ))
    if num > numberRandom:
        print('Maior que o correto \n')
    elif num < numberRandom:
            print('Menor que o correto \n')
    elif num == numberRandom :
        print('VOCÊ ACERTOU')
        break





