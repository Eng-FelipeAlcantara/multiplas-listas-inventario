equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 'S'

while resposta == 'S':
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valor: ')))
    seriais.append(int(input('serial: ')))
    departamentos.append(input('Departamento: '))
    resposta = input('Digite S para continuar: ').upper()

for equipamento in equipamentos:
    print('Equipamento: ', equipamento)
    resposta = input('Digite S para continua: ').upper()