cont = 0
num = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]:'))
    if num != 999:
      cont += 1
      soma += num
else:
     print(f'Você digitou {cont} números e a soma entre eles foi {soma}. ')
