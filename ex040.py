n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
media=(n1+n2)/2
print(f'Tirando a média de {n1} e {n2},a média do aluno é {media}.')

if media < 5:
    print('O aluno está REPROVADO!')

elif 5 <= media <6.9:
    print('O aluno está em RECUPERAÇÃO!')

else:
    print('O aluno está APROVADO!')

