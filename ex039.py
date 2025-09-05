from datetime import date

atual = date.today().year
nasc = int(input('Digite o ano em que você nasceu: '))
idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')

elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} {"ano" if saldo == 1 else "anos"}.')

else:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Ainda falta {saldo} {"ano" if saldo == 1 else "anos"} para o seu alistamento.')
    print(f'Seu alistamento será em {ano}.')




