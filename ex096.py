def area(comp,larg):
    area = comp * larg
    print(f'A área de um terreno {larg}m x {comp}m é de {area}m².')


print('Controle de Terrenos')
print('-' * 20)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(comp,larg)




