km=int(input('Digite a distância da viagem: '))
valor1=0.50*km
valor2=0.45*km
if km <= 200:
    print(f'O valor da sua passagem ficou R${valor1:.2f}.')
else:
    print(f'O valor da sua passagem ficou R${valor2:.2f}.')
