salario_bruto = input('Digite o salário bruto, em R$: ')
ir_desconto = float(salario_bruto)*0.11
inss_desconto = float(salario_bruto)*0.08
sindicato_desconto = float(salario_bruto)*0.05
salario_liquido = float(salario_bruto)-ir_desconto-inss_desconto-sindicato_desconto

print(f'Salário bruto: R${salario_bruto}\n'
      f'IR(11%): R${ir_desconto}\n'
      f'INSS(8%): R${inss_desconto}\n'
      f'Sindicato(5%): R${sindicato_desconto}\n'
      f'Salário líquido: R${salario_liquido}')