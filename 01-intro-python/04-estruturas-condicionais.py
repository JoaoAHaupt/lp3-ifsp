# if,if/else, else, elif, ternario, match

# if
# if condicao:
#   corpo

idade = 20
if idade >= 10:
    print('Mais de uma decada de idade!')
else:
    print('noob')

# criança (0-12) adolescente(13-17) adulto(18-59) idoso(60+)
if idade <=12:
    print('C')
elif idade <= 17:
    print('Ad')
elif idade<=59:
    print('adul')
else:
    print('Idoso')

# if alinhado (evitar)
email = 'joao@email.com'
senha= 'amominhanamorada'

if email == 'joao@email.com' and senha == '123123123':
        print('Acesso liberado')
else:
    print('Senha ou email incorretos')

# condição complexa no if
# permirtir a entrada se: o usuario não estiver bloqueado E o usuario for um funcionario E hora atual entre 08 e 18 OU o usuario é adm

usuario_bloqueado = False
usuario_funcionario = True
hora_atual = 19
usuario_adm = False

# variaveis
horario_comercial = hora_atual >= 8 and hora_atual <= 19
usuario_ativo = not usuario_bloqueado and usuario_funcionario
liberado = (usuario_ativo and horario_comercial) or usuario_adm

if liberado:
     print('Acesso liberado')
else:
     print('Acesso negado')                                                                  

# entrada: hora_atual
# saída: bool

def dentro_do_horario_comercial (hora_atual):
     return hora_atual>=8 and hora_atual <= 18


# Operador ternario
if idade >= 18:
     status = 'maior'
else:
     status ='menor'

status = 'maior' if idade >= 18 else 'menor'

# usuario passa o dia (int
# devolve string nome
# 1- domingo, 2 - segunda, ..

dia = 4
dias = {
     1: 'Domingo',
     2: 'Segunda',
     3: 'Terça',
     4: 'Quarta',
     5: 'Quinta',
     6: 'Sexta',
     7: 'Sábado'
}

if dia in dias:
     print(dias[dia])

# match
# python 3.10

dia = 2
match dia:
    case 1 | 7:
        print('FDS')
    case 2 | 3 |4 |5 |6 :
        print('Dia util')
    case _:
          print('Inválido')