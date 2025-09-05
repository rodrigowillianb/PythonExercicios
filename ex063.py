print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
termo = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} ➜ {t2}', end=' ➜ ')
cont = 3
while cont <= termo:
    t3 = t1 + t2
    print(f'{t3}', end=' ➜ ' if cont < termo else '')
    t1 = t2
    t2 = t3
    cont += 1


