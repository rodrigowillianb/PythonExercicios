lista = []

while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Não vou adicionar.")

    r = input("Quer continuar? [S/N] ")
    if r not in "nN":
        break

print("-=" * 30)
print(f"Você digitou os valores: {sorted(lista)}")
