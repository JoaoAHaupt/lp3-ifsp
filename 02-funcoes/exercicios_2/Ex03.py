'''
Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.
'''
import unicodedata 
import re

frase = unicodedata.normalize('NFKD' , input('Entre com uma frase: ').lower()).encode('ASCII', 'ignore').decode('ASCII').strip().replace(" ", "")
frase2 = re.sub(r"[,;&!?/.:]", frase, "")

vogais = 0
for letra in frase:
    if letra == 'a' or letra == 'e' or letra == 'u' or letra == 'i' or letra == 'o':
        vogais = vogais + 1

consoantes = 0
if(vogais >=len(frase)):
    consoantes = vogais - len(frase)
else:
    consoantes = len(frase) - vogais

print(f'Sua frase tem {vogais} vogais e {consoantes} consoantes')



