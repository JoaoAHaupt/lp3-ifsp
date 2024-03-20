'''
Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e 
verifique se é um palíndromo (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).
'''

frase = input('DIGITE UMA FRASE')
metade = 0
print(len(frase))
if(len(frase) % 2 == 0):
    metade = len(frase) - 1


for i in (0, metade, 1):
    for j in range(len(frase)-1, metade, -1):
        if(frase[i] != frase[j]):
            print('ERROR')
            break
        else:
            print('certoo')