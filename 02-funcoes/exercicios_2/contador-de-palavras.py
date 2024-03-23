
frase = input("Digite a frase: ").split(' ')

dicionario = {}

for i in range(0, len(frase), 1):
    if frase[i] in dicionario:
        dicionario[frase[i]] = 1 + dicionario[frase[i]]
    else:
        dicionario[frase[i]] = 1

print(dicionario)