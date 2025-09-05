print("======== LOJAS BATISTA ========")
compras = float(input('Preço das compras:R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opção=int(input('Qual a opção? '))

if opção == 1:
    print(f'Sua compra de R${compras:.2f} vai custar R${compras*0.9:.2f}.')

elif opção == 2:
    print(f'Sua compra de R${compras:.2f} vai custar R${compras*0.95:.2f}. ')

elif opção == 3:
    print(f'Sua compra será parcelada em 2x de R${compras/2:.2f}.')

elif opção ==4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcelas}x de R${compras/parcelas:.2f} COM JUROS ')
    print(f'Sua compra de R${compras:.2f} vai custar R${compras * 1.20:.2f} com o acréscimo de 20% de juros.')

