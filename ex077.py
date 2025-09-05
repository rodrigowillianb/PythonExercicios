from time import sleep
palavras = ('aprender','programar','linguagem','python','curso',
            'gratis','estudar','praticar','trabalhar','mercado',
            'programador','futuro')

print('Neste programa será mostrado as vogais de cada palavra:')
sleep(1.5)
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end= ' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')


