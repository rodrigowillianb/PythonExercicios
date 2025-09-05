lanche = ('Hámburguer' ,'Suco' , 'Pizza' , 'Pudim')
#print(sorted(lanche))

#for cont in range (0,len(lanche)):
 #   print(f'Eu vou comer {lanche[cont]}')

#for comida in lanche:
 #   print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

a = (2,5,4)
b = (5,8,1,4)
c = b + a
print(c.index(8))
del(lanche)