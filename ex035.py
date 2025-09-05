print('-=-'*20)
print('Analisador de triângulos')
print('-=-'*20)
num1=float(input('Primeiro segmento: '))
num2=float(input('Segundo segmento: '))
num3=float(input('Terceiro segmento: '))
if num1 < num2+num3 and num2 < num1+num3 and num3 < num1+num2:
    print('Os segmentos podem formar um triângulo.')
else:
    print('Os segmentos não podem formar um triângulo. Digite outros segmentos.')


