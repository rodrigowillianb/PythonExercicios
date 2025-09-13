alunos = []
while True:
    nome=(input('Nome: ')).upper()
    nota1=(float(input('Nota 1: ')))
    nota2=(float(input('Nota 2: ')))
    aluno = [nome,nota1,nota2]
    alunos.append(aluno[:])
    continuar=(input('Quer continuar? [S/N]: '))
    if continuar not in 'Ss':
        break

print('-=' * 20)
print(f'{"Nº":<3} {"NOME":<10} {"MÉDIA":>6}')
print('-' * 20)

for i, aluno in enumerate(alunos):
    media = (aluno[1] + aluno[2]) / 2
    print(f'{i:<3} {aluno[0]:<10} {media:>6.1f}')
print('-' * 20)

while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(alunos) -1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]} e {alunos[opc][2]}')
print('<<< VOLTE SEMPRE >>>')











