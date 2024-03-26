'''
Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.
'''
import unicodedata 
import re
frase = unicodedata.normalize('NFKD', input('Entre com uma frase: ').lower()).encode('ASCII', 'ignore').decode('ASCII').strip().replace(" ", "")
frase = re.sub(r'[^\w\s]', '', frase)
frase = ''.join(c for c in frase if not c.isdigit())

vogais = 0
for letra in frase:
    if letra in 'aeiou':
        vogais = vogais + 1

consoantes = len(frase) - vogais

print(f'Sua frase tem {vogais} vogais e {consoantes} consoantes')



