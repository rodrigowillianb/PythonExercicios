from datetime import date
ano_atual = date.today().year

pessoa = {}

while True:
    nome = input('Nome: ')
    pessoa['nome'] = nome
    ano_nascimento = int(input('Ano de Nascimento: '))
    pessoa['idade'] = ano_atual - ano_nascimento
    carteira_de_trabalho = (int(input('Carteira de trabalho (0 não tem): ')))
    pessoa['ctps'] = carteira_de_trabalho
    if carteira_de_trabalho == 0 :
        print('=-' * 30)
        print(f'O nome da pessoal é {pessoa["nome"]};')
        print(f'Idade:{pessoa["idade"]} anos;')
        print(f'CTPS:{pessoa["ctps"]}')
        break
    else:
        ano_contratação = int(input('Ano de contratação: '))
        pessoa['aposentadoria'] = pessoa['idade'] + ((ano_contratação + 35) - ano_atual)
        pessoa['ano_contratação'] = ano_contratação
        salário = float(input('Salário:R$'))
        pessoa['Salário'] = salário
        print('=-' * 30)
        print(f'O nome da pessoal é {pessoa["nome"]};')
        print(f'Idade:{pessoa["idade"]} anos;')
        print(f'CTPS:{pessoa["ctps"]}')
        print(f'O ano de contratação foi em {ano_contratação};')
        print(f'O salário é R${salário};')
        print(f'{nome} vai se aposentar com {pessoa['aposentadoria']} anos.')
        break











