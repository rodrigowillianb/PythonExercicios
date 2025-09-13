matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_impares = 0

for linha in range(3):
    for coluna in range(3):
        n = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha][coluna] = n

        if n % 2 == 0:
            soma_pares += n
        else:
            soma_impares += n

print('-=' * 20)

for linha in matriz:
    print(linha)

print('-=' * 20)
print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos valores ímpares é {soma_impares}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')


