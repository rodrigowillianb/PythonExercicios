dados = {}

n = (input('Nome: '))
dados['nome'] = n

m = float(input(f'Média de {n}: '))
dados['média'] = m

print('=-' * 30)
print(f'O nome é do aluno é {dados["nome"]};')
print(f'A média do aluno é {dados["média"]};')

if m < 7:
    print(f'{n} está de RECUPERAÇÃO!')
else:
    print(f'{n} está APROVADO,PARABÉNS!')




