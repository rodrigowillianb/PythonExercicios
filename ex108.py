from Módulos.uteis import numeros

p = float(input('Digite o preço: R$'))


print(f'A metade de R${p} é R${numeros.metade(p)}.')
print(f'O dobro de R${p} é R${numeros.dobro(p)}.')
print(f'Aumentando 10%, temos R${p + numeros.fracão(p)}.')