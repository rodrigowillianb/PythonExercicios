from time import sleep
num = int(input('Digite um número para calcular seu Fatorial:'))
c = num
f = 1
print(f'Calculando {num}!= ',end ='')
sleep(1.3)
while c > 0:
    print(f'{c}',end='')
    print('x' if c > 1 else '=', end='')
    f *= c
    c -= 1
print(f'{f}')


