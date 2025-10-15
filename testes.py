def falar():
    print('Olá, Humano!')

def pessoa():
    nome = input('Qual o seu nome: ')
    return nome

falar()
nome = pessoa()
print(f'Muito prazer, {nome}!')
