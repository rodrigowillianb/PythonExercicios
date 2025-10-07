from time import sleep
import random

def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for i in range(5):
        num = random.randint(1, 10)
        lista.append(num)
        print(num, end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')

def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}.')

# Programa principal
numeros = []
sorteia(numeros)
soma_par(numeros)
