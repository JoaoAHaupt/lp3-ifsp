'''
Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e 
verifique se é um palíndromo (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).
'''
import re

# tirar a acentuação

frase = input().lower().replace(' ', '')
frase = re.sub(r'[^\w\s]', '', frase)
reverse = ''.join(reversed(frase))

if frase == reverse:
    print('Palindromo')
else:
    print('normie')
print(frase)
print(reverse)