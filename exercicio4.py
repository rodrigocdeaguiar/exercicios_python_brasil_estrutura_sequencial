nota1 = input('Digite um valor da nota do 1° bimestre: ')
nota2 = input('Digite um valor da nota do 2° bimestre: ')
nota3 = input('Digite um valor da nota do 3° bimestre: ')
nota4 = input('Digite um valor da nota do 4° bimestre: ')

media_anual = (float(nota1) + float(nota2) + float(nota3) + float(nota4))/4
print(f'Média anual: {media_anual:.1f}')