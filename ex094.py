pessoas = []
mulheres = []

while True:
    pessoa = {}  # cria um novo dicionário para cada pessoa
    pessoa['nome'] = input('Nome: ')

    # Validação do sexo
    while True:
        sexo = input('Sexo [M/F]: ').strip().upper()
        if sexo in ('M', 'F'):
            pessoa['sexo'] = sexo
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa)  # adiciona o dicionário à lista

    # Se for mulher, adiciona à lista de mulheres
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('=-' * 30)
print(f'A)Ao todo temos {len(pessoas)} pessoas cadastradas.')

soma = sum(p['idade'] for p in pessoas)
media = soma/len(pessoas)
print(f'B)A média de idade é de {media:.1f} anos.')

print(f'C)As mulheres cadastradas foram:',mulheres)

print('D) Lista das pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] > media:
        print(f"    Nome = {p['nome']}; Sexo = {p['sexo']}; Idade = {p['idade']}")
















