print('=' * 30)
print('          BANCO CEV')
print('=' * 30)

cedulas = [50, 20, 10, 1]
valor = int(input('Qual valor você quer sacar? R$ '))

i = 0
while valor > 0 and i < len(cedulas):
    ced = cedulas[i]
    qtd, valor = divmod(valor, ced)
    if qtd > 0:
        print(f'{qtd} nota(s) de R${ced}.')
    i += 1







