jogadores = {}

jogador = input('Nome do jogador: ')
jogadores['nome'] = jogador

partida = int(input(f'Quantas partidas {jogador} jogou? '))

gols = []
for g in range(partida):
    gol =int(input(f'Quantos gols na partida {g}? '))
    gols.append(gol)

jogadores['gols'] = gols
jogadores['total'] = sum(gols)

print('=-' * 30)
print(jogadores)
print('=-' * 30)
for c,v in jogadores.items():
    print(f'O campo {c} tem o valor {v};')
jogadores['partidas'] = partida
print('=-' * 30)
print(f'O jogador {jogadores["nome"]} jogou {jogadores["partidas"]} partidas.')
for p,q in enumerate(gols):
    print(f'=> Na partida {p},fez {q} gols.')
print(f'Foi um total de {jogadores["total"]} gol(s).')






