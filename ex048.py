from time import sleep
soma = 0
cont = 0
for n in range (1,501,2):
    if n % 3 == 0:
        cont = cont + 1
        soma = soma + n
print('Calculando a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500: ')
sleep(1)
print('=' * 111)
sleep(2)
print(f'A soma de todos os valores solicitados é {soma} !')