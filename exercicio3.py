num1 = input('Digite um número inteiro: ')
num2 = input('Digite outro número inteiro: ')


if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    soma = num1 + num2
    print(f'Soma = {soma}')
else:
    print(f'Valores inválidos!')