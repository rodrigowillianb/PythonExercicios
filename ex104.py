def leiaint(msg):
    while True:
        n = input(msg)
        if n.strip().lstrip('-').isdigit():
            return int(n)
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


#Programa principal
n = leiaint('Digite um número:')
print(f'\033[32mVocê acabou de digitar o número {n}.\033[m')


