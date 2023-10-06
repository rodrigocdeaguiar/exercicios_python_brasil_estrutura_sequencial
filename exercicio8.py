valor_hora = input('Digite o valor de sua hora/atividade em R$: ')
horas_atividade = input('Digite a quantidade de horas que você trabalhou: ')

salario_mes = float(valor_hora)*int(horas_atividade)

print(f'O seu salário do mês é R${salario_mes:.2f}')
