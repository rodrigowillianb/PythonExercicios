from time import sleep
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
print('Processando...')
sleep(1.5)
opção = 0

while opção != 5:
    print('=-=' * 10)
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opção = int(input('Qual é a sua opção?'))
    if opção == 1:
        soma = n1 + n2
        print('Calculando...')
        sleep(1.5)
        print(f'A soma entre {n1} e {n2} é {soma}.')
        sleep(3)
    elif opção == 2:
        multiplicação = n1 * n2
        print('Multiplicando...')
        sleep(1.5)
        print(f'O resultado de {n1} X {n2} é {multiplicação}.')
        sleep(3)
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Buscando resultado...')
        sleep(2)
        print(f'Entre {n1} e {n2} o maior é {maior}!')
        sleep(3)

    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor:'))
        sleep(1)
        n2 = int(input('Segundo valor:'))
        sleep(1)

    elif opção == 5:
        print('Finalizando...')

    else:
        print('Opção inválida. Tente novamente.')
        sleep(2.4)
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')

