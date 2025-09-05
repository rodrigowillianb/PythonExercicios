num1=int(input('Digite um numero: '))
num2=int(input('Digite outro numero: '))
num3=int(input('Digite mais um numero: '))
if num1<num2 and num1<num3:
    print(f'O menor valor digitado foi {num1}')
if num2<num1 and num2<num3:
    print(f'O menor valor digitado foi {num2}')
if num3<num1 and num3<num2:
    print(f'O menor valor digitado foi {num3}')
if num1>num2 and num1>num3:
    print(f'O maior valor digitado foi {num1}')
    if num2>num1 and num2>num3:
        print(f'O maior valor digitado foi {num2}')
        if num3>num1 and num3>num2:
            print(f'O maior valor digitado foi {num3}')
