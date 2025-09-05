print('-' * 30)
print('     CADASTRE UMA PESSOA')
print('-' * 30)
tot18=0
tothomens=0
mulheres20=0
cont = 0
continuar='S'
while True:
 idade=int(input('Idade:'))
 cont += 1
 sexo=str(input('Sexo: [M/F] ' )).strip().upper()[0]
 if idade > 18:
     tot18 += 1
 if sexo =='M':
     tothomens += 1
 if sexo =='F' and idade < 20:
    mulheres20 += 1
 print('-' * 30)
 continuar=(str(input('Quer continuar? [S/N] ')).strip().upper()[0])
 if continuar =='N':
     break
print(f'Total de pessoas com mais de 18 anos:{tot18}')
print(f'Ao todo temos {tothomens} homens cadastrados')
print(f'E temos {mulheres20} mulheres com menos de 20 anos.')




