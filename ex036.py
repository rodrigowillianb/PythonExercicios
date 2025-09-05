"""
Este programa aprova ou nega um empréstimo bancário para a compra de uma casa.
Ele solicita ao usuário:
- O valor da casa
- O salário do comprador
- A quantidade de anos para pagamento

A prestação mensal não pode exceder 30% do salário do comprador,
caso contrário, o empréstimo será negado.
"""
casa = float(input('Digite o valor da casa: R$'))
salário = float(input('Digite o salário do comprador: R$'))
anos = int(input('Digite em quantos anos irá ser pago: '))
prestação = casa / (anos * 12)

if prestação > (salário * 0.30):
    print('Empréstimo negado devido a prestação ser maior que 30% do salário!')
else:
    print(f'Empréstimo aprovado! Para pagar uma casa de R${casa:.2f} em {anos} anos, a prestação será de R${round(prestação,2)}')






