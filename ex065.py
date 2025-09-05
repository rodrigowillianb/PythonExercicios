resp = 'S'
cont = 0
num = 0
soma = 0
maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número:'))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar?')).upper().strip()[0]
media = soma / cont
print(f'Você digitou {cont} números e a média entre eles foi de {media:.2f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
