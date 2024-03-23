'''
Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma palavra oculta (o usuário não vê) e o usuário tenta adivinhar a palavra, letra por letra.
       O usuário tem um número limitado de tentativas para adivinhar toda a palavra.
'''

vermelho = "\033[91m"
verde = "\033[92m"
cor = "\033[0m"
texto_verde = verde + 'Letras corretas: ' + cor
texto_vermelho = vermelho + 'Letras erradas: ' + cor
palavra_secreta = 'LATORRE'
segredo = list('_______')
letras = []
letras_incorretas = []
tentativas_restantes = 7
prints_forcas = {
    7: ['______     ', '|    I     ' ,'|          ','|          ','|          ','|          ', '----       '],
    6: ['______     ', '|    I     ' ,'|    O     ','|          ','|          ','|          ', '----       '],
    5: ['______     ', '|    I     ' ,'|    O     ','|    |     ','|          ','|          ', '----       '],
    4: ['______     ', '|    I     ' ,'|    O     ','|   /|     ','|          ','|          ', '----       '],
    3: ['______     ', '|    I     ' ,'|    O     ','|   /|\    ','|          ','|          ', '----       '],
    2: ['______     ', '|    I     ' ,'|    O     ','|   /|\    ','|   /      ','|          ', '----       '],
    1: ['______     ', '|    I     ' ,'|    O     ','|   /|\    ','|   / \    ','|          ', '----       '],

}

def forca(tentativa):
    if tentativa in prints_forcas:
        for forca_print in prints_forcas[tentativa]:
            print(forca_print)



while True:
    iguais = []

    print(f'Tentativas restantes {tentativas_restantes}')

    forca(tentativas_restantes)

    lista_incorretas = ', '.join(letras_incorretas)
    print(texto_vermelho + lista_incorretas )

    lista_corretas = ', '.join(letras)
    print(texto_verde + lista_corretas + '\n')

    print(''.join(segredo))

    tentativa = input('Entre com uma letra ').upper().strip()

    if len(tentativa) > 1 or not tentativa.isalpha():
        print('TENTATIVA INVÁLIDA \n')
    elif tentativa in letras or tentativa in letras_incorretas:
        print('Você já tentou essa letra! \n')
    elif tentativa in palavra_secreta:
        letras.append(tentativa)
        for i in range(0, len(palavra_secreta), 1):
            if palavra_secreta[i] == tentativa:
                iguais.append(i)
        for i in range(len(palavra_secreta)):
            if i in iguais:
                segredo[i] = tentativa
    else:
        letras_incorretas.append(tentativa)
        tentativas_restantes = tentativas_restantes - 1
        if tentativas_restantes == 0:
            print('\n' * 6)
            print(f'Você perdeu :(! A palavra secreta era: {palavra_secreta}!')
            print('\n' * 6)

            break

    if palavra_secreta == ''.join(segredo):
        print('\n' * 6)
        print(f'VOCÊ GANHOU!!! :)) A palavra secreta era: {palavra_secreta}!')
        print('\n' * 5)
        break






