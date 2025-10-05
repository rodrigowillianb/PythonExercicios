jogadores = []

while True:
    jogador = {}
    jogador['nome'] = input('Nome do jogador: ')

    partida = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    gols = []
    for g in range(partida):
        gol = int(input(f'Quantos gols na partida {g+1}? '))
        gols.append(gol)

    jogador['gols'] = gols
    jogador['total'] = sum(gols)

    jogadores.append(jogador.copy())

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('=-' * 30)
print(f'{"cod":<4} {"nome":<15} {"gols":<15} {"total":<5}')
print('-' * 40)

for i, j in enumerate(jogadores):
    print(f'{i:<4} {j["nome"]:<15} {str(j["gols"]):<15} {j["total"]:<5}')

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}:')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-' * 40)

print('<< VOLTE SEMPRE >>')





