'''
Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e 
verifique se é um palíndromo (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).
'''
import re
import unicodedata

frase = input('Digite uma frase: ')
frase = unicodedata.normalize('NFD', frase)
frase = frase.encode('ascii', 'ignore').decode('utf-8')
frase = re.sub(r'[^\w\s]', '', frase.lower().replace(' ', ''))
reverse = ''.join(reversed(frase))

print(frase)
print(reverse)

if frase == reverse:
    print('A frase é um palíndromo!')
else:
    print('A frase NÃO é um palíndromo!')
