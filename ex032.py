import datetime

ano = int(input('Qual ano você quer analisar? '))
if ano == 0:
    ano = datetime.date.today().year

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')

