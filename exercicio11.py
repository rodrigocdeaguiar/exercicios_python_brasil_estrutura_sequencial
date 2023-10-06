n1 = input('Digite um número inteiro: ')
n2 = input('Digite outro número inteiro: ')
n3 = input('Digite um número real: ')

calc1 = (int(n1)*2)/(int(n2)/2)
calc2 = (int(n1)*3)+float(n3)
calc3 = float(n3)**3

print(f'O produto do dobro do primeiro com metade do segundo é {calc1:.2f}')
print(f'A soma do triplo do primeiro com o terceiro é {calc2:.2f}')
print(f'o terceiro elevado ao cubo é {calc3:.2f}')