from datetime import date
atual = date.today().year

cont_maiores = 0
cont_menores = 0

for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        cont_maiores += 1
    else:
        cont_menores += 1

print(f'Ao todo tivemos {cont_maiores} pessoas maiores de idade.')
print(f'E também tivemos {cont_menores} pessoas menores de idade.')
