soma = 0
pessoa = 4
maioridade = 0
homemmaisvelho = ''
cont_mulheres_menor_20 = 0

for p in range(1, 5):
    print(f"{'-' * 5} {p}ª PESSOA {'-' * 5} ")
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma += idade

    if sexo == 'M':
        if idade > maioridade:
            maioridade = idade
            homemmaisvelho = nome

    if sexo == 'F' and idade < 20:
        cont_mulheres_menor_20 += 1

media = soma / pessoa
print(f'A média de idade do grupo é de {media:.1f} anos.')

if homemmaisvelho != '':
    print(f'O homem mais velho é {homemmaisvelho} com {maioridade} anos.')
else:
    print('Não há homens no grupo.')

print(f'Ao todo são {cont_mulheres_menor_20} mulheres com menos de 20 anos.')
