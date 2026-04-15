from Módulos.uteis import numeros

p = float(input('Digite o preço: R$'))


print(f'A metade de {numeros.moeda(p)} é {numeros.moeda(numeros.metade(p))}.')
print(f'O dobro de {numeros.moeda(p)} é {numeros.moeda(numeros.dobro(p))}.')
print(f'Aumentando 10%, temos {numeros.moeda(numeros.fracão(p))}.')
