def area(comp,larg):
    area = comp * larg
    print(f'A área de um terreno {comp}m x {larg}m é de {area}m².')


print('  Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float (input('COMPRIMENTO (m): '))
area(l,c)








