times = ('Flamengo' , 'Cruzeiro', 'Palmeiras', 'Bahia', 'Botafogo',
         'São Paulo', 'Mirassol', 'Fluminense', 'Bragrantino', 'Ceará',
         'Atlético-MG', 'Internacional','Corinthians', 'Santos','Grêmio',
         'Vasco','Vitória','Juventude','Fortaleza','Sport')

print('-=' * 20)
print(f'Lista de times do Brasileirão:{times}')
print('-=' * 20)
print ('Os 5 primeiros são',end ='')
print(times[0:6])
print('-=' * 20)
print('Os 4 últimos são',end = '')
print(times[16:21])
print('-=' * 20)
print('Times em ordem alfabética:',sorted(times))
print(f'O Botafogo está na {times.index('Botafogo')+1} posição.')