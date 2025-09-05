#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km=float(input('Quantos Km foram percorridos com o carro alugado ? '))
dias=int(input('Esse carro foi alugado por quantos dias?'))
valor=(60 * dias)+ (0.15*km)
print(f'O valor do aluguel do carro foi de R${valor:.2f}.')


