peso_maior = 0
peso_menor = 0

for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        # Na primeira pessoa, inicializa ambos com o mesmo peso
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso

print(f'O maior peso lido foi {peso_maior} kg.')
print(f'O menor peso lido foi {peso_menor} kg.')
