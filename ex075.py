from collections import Counter

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite mais número:'))
n4 = int(input('Digite o último número:'))
valores = (n1,n2,n3,n4)
par = 0
print(f'Você digitou os valores {valores}')

# Conta quantas vezes cada valor aparece
contagem = Counter(valores)

# Filtra só os repetidos
repetidos = {num:qtd for num, qtd in contagem.items() if qtd >1}

if repetidos:
    for num, qtd in repetidos.items():
        print(f'O número {num} aparece {qtd} vezes.')
    else:
        pass

print(f'O valor {n2} apareceu na posição {valores.index(n2)+1}.')

pares = [n for n in valores if n % 2 == 0]

print(f'Os valores pares digitados foram {pares}')



