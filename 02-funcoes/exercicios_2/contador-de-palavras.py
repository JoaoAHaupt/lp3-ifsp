import re

frase = input("Digite a frase: ")
frase = re.sub(r'[^\w\s]', '', frase).split()


dicionario = {}

for palavra in frase:
    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1

print("Dicionário de contagem de palavras:")
print(dicionario)


