import random
from time import sleep
cont=0

print('Sou seu computador...')
sleep(1.3)
print('Vou pensar em um número entre 0 e 10.')
sleep(1.3)
print('-=-' * 20)
sleep(1.3)

random_number = random.randint(0, 10)

print('Será que você consegue adivinhar qual foi?...')
sleep(1.5)

num = int(input('Em que número eu pensei?:'))
cont+=1

while num != random_number:
    if num < random_number:
        num = int(input('Mais... Tente mais uma vez: '))
    elif num > random_number:
        num = int(input('Menos... Tente mais uma vez: '))
    cont+=1

print(f'UAU! Você acertou em {cont} tentativas! Parabéns!')
