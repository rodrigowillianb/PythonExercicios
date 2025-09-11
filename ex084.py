lista = []

while True:
    nome = input('Digite um nome: ')
    peso = float(input('Peso: '))
    lista.append([nome, peso])

    r = input('Quer continuar? [S/N] ')
    if r not in 'Ss':
        break


maipeso = menpeso = lista[0][1]  # começa com o primeiro peso
for pessoa in lista:
    if pessoa[1] > maipeso:
        maipeso = pessoa[1]
    if pessoa[1] < menpeso:
        menpeso = pessoa[1]

print('=-' * 30)
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maipeso}Kg. Peso de ', end='')
for pessoa in lista:
    if pessoa[1] == maipeso:
        print(f'[{pessoa[0]}]', end='')
print()
print(f'O menor peso foi de {menpeso}Kg. Peso de ', end='')
for pessoa in lista:
    if pessoa[1] == menpeso:
        print(f'[{pessoa[0]}]', end=' ')
print()
