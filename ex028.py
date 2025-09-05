import random
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
random_number = random.randint(0, 5)  # Gera um número aleatório entre 0 e 5
num = int(input('Em que número eu pensei? Digite aqui: '))
print('-=-'*20)
print('PROCESSANDO...')
sleep(2)

if num == random_number:
    print('UAU! Você acertou!')
else:
    print(f'Você errou! Eu pensei no número {random_number}. Tente novamente!')



