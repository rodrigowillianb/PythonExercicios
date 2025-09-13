lista = [[],[]]

for c in range (1,8):
      n = int(input(f'Digite o {c}° valor: '))
      if n % 2 == 0 :
          lista[0].append(n)
      else:
          lista[1].append(n)

print('=-' * 30)
lista[0].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
lista[1].sort()
print(f'Os valores ìmpares digitados foram: {lista[1]}')
print('=-' * 30)



