nome_pescador = input('Digite o nome do pescador: ')
peso_peixes = input('Digite a quantidade de peixes pescado, em kg: ')

if float(peso_peixes) < 0:
    print('Valor de peso inválido!')
elif 0 <= float(peso_peixes) <= 50:
    print('Não há multa a ser paga por peso excedente.')
elif float(peso_peixes) > 50:
    peso_excedente = float(peso_peixes) - 50
    valor_multa = peso_excedente*4
    print(f'Sr(a). {nome_pescador}, a multa paga por peso excelente é R${valor_multa:.2f}.')