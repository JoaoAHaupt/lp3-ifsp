'''
x06 - Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100),
converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.
'''

nota = int(input('Entre com sua nota de 0 a 100 '))


def conversor(pontuacao):
    if pontuacao > 100 or pontuacao < 0:
        return 'PONTUAÇÃO INVÁLIDA'
    elif pontuacao >= 90:
        return 'A'
    elif pontuacao >= 80:
        return 'B'
    elif pontuacao >= 70:
        return 'C'
    elif pontuacao >= 60:
        return 'D'
    else:
        return 'F'


print(f'Você tirou: {conversor(nota)}')
