'''
Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos. O programa deve pedir ao usuário para votar várias vezes e, no final, 
mostrar o número de votos de cada candidato e quem foi o vencedor. 
'''
print('VOTE NOS SEGUINTES CANDIDATOS \n Latorre do Povo: 34 \n Quirino de taubate: 98 \n Motta do fundão: 92')
i = 0
canditados = [0,0,0]

for i in range(12):
    voto = int (input('Coloque o número do seu candidato: '))
    if(voto == 34):
        print(' *PLIN PLIN PLIN * Voto computado LATORRE')
        canditados[0] = canditados[0]+1
    elif(voto == 98):
        print(' *PLIN PLIN PLIN * Voto computado QUIRINO')
        canditados[1] = canditados[1]+1
    elif(voto == 92):
        print(' *PLIN PLIN PLIN * Voto computado MOTTA')
        canditados[2] = canditados[2]+1
    else:
        print(' *PLIN PLIN PLIN * Voto computado BRANCO')


num_votos = max(canditados)
if(canditados[0] == num_votos):
    print('LATORRE GANHOU')
elif(canditados[1] == num_votos):
    print('QUIRINO GANHOU')
else:
    print('MOTTA GANHOU')
