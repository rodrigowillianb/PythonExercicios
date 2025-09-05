from datetime import date
atual = date.today().year
nasc=int(input('Digite o ano em que você nasceu:'))
idade= atual-nasc

print(f'O atleta tem {idade} anos.')

if idade <=9:
    print('Classificação: MIRIM')

elif 9 < idade <15:
    print('Classificação: INFANTIL')

elif 14 < idade <20:
    print('Classificação: JÚNIOR')

elif  19 < idade <26:
    print('Classificação: SÊNIOR')

elif idade > 25:
    print('Classificação: MASTER')


