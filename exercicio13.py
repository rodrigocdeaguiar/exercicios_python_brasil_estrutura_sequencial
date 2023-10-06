altura = input('Digite a sua altura, em m: ')
genero = input('Digite 1, caso você seja homem ou digite 2, caso você seja mulher: ')

if genero == '1':
    peso_ideal = (72.7*float(altura))-58
elif genero == '2':
    peso_ideal = (62.1 * float(altura)) - 44.7
else:
    print('Valor para gênero inválido.')

print(f'Seu peso ideal é {peso_ideal:.2f} kg.')
