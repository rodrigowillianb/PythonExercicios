def validacao(jogador, gols):
    if jogador == '':
        jogador = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


print('-=' * 20)
nome = str(input('Nome do jogador: '))
gols = input('Número de gols: ')

# Verifica se o número é digitado corretamente
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

validacao(nome, gols)
