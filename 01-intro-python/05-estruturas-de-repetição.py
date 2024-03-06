# for, while, (break,continue)

for letra in 'Olá Mundo':
    print(letra)

prontuarios = ['SP001', 'SP002', 'SP003']

for prontuario in prontuarios:
    print(prontuario)

# range(5) => 0, 1, 2, 3, 4
for i in range(5):
    print(i)
#          start stop step 
for i in range(0, 12, 2):
    print(i)

lista = list(range(1, 101))
print(lista)

# while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Break
comando = ''    
while True:
    comando = input('Digite o comando \n')
    if comando == 'Sair':
        break;


#compreendendo listas
numeros = [1,0,-23,-2,-123,8,2]
positivos = [numero for numero in numeros if numero > 0]
elevado_quad = [numero**2 for numero in numeros]
print(positivos)
print(elevado_quad)