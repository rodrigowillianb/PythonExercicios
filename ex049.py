from time import sleep
n1 = int(input('Digite um valor para mostrar sua tabuada:'))
for c in range(1, 11):
    print(f'{n1} x {c} = {n1 * c}')
    sleep(0.5)
