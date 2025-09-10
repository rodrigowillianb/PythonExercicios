lista = []

while True:
    n = int(input('Digite um valor:'))
    if n not in lista:
        lista.append(n)
    r = input('Quer continuar? [S/N]:')
    if r not in 'sS':
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort()
lista.reverse()
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')