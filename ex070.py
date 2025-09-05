print('-' * 30)
print('     LOJA SUPER BARATÃO')
print('-' * 30)
totcompras = 0
prod1000 = 0
menor_preco = None
produto_mais_barato = ''

while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Preço: R$ '))
    totcompras += valor

    if valor > 1000:
        prod1000 += 1

    if menor_preco is None or valor < menor_preco:
        menor_preco = valor
        produto_mais_barato = produto

    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print('------------ FIM DO PROGRAMA ------------.')
print(f'O total da compra foi R${totcompras:.2f}')
print(f'Temos {prod1000} produtos custando mais de R$1000.00.')
print(f'O produto mais barato foi {produto_mais_barato} custando R${menor_preco}.')

