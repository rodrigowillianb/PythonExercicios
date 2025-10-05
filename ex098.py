from time import sleep

def contagem(inicio, fim, passo):
    """Faz uma contagem entre dois números com pausa e passo configurável."""

    # Evita passo 0
    if passo == 0:
        passo = 1
    # Garante passo positivo (só para usar no cálculo)
    passo = abs(passo)

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')

    # Contagem crescente ou decrescente
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
            sleep(0.3)
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ')
            sleep(0.3)

    print('FIM!')
    print('-=' * 20)
    sleep(0.6)


# Programa principal
contagem(1, 10, 1)
contagem(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contagem(inicio, fim, passo)










