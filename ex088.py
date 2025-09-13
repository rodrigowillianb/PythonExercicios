import random
from time import sleep

print('-' * 30)
print('      JOGO DA MEGA SENA ')
print('-' * 30)

n = int(input('Quantos jogos você quer que eu sorteie? '))

if n > 0:
    print('-=' * 3, f'SORTEANDO {n} JOGOS', '-=' * 3)
    for i in range(n):
        jogo = random.sample(range(1, 61), 6)
        sleep(1.0)
        jogo.sort()
        print(f'Jogo {i + 1}: {jogo}')
    print('-=' * 15)
else:
    print('Número de jogos inválido.')








