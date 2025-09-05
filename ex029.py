velocidade=int(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print(f'MULTADO!Você excedeu o limite permitido de 80km/h! Você deve pagar uma multa de R${multa:.2f}.')
print('Tenha um bom dia! Dirija com segurança!')



