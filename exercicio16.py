area_pintada = (input('Digite a área a ser pintada, em m2: '))

cobertura_lata_tinta = 18*3
preco_lata_tinta = 80

if float(area_pintada) <= cobertura_lata_tinta:
    print(f'Será necessária uma lata de tinta. Valor total da compra: R${preco_lata_tinta},00.')
if float(area_pintada) > cobertura_lata_tinta:
    if float(area_pintada)%cobertura_lata_tinta == 0:
        latas_tinta = (float(area_pintada)/cobertura_lata_tinta)
        valor_compra = latas_tinta * preco_lata_tinta
    else:
        latas_tinta = int((float(area_pintada)/cobertura_lata_tinta)+1)
        valor_compra = latas_tinta * preco_lata_tinta
    print(f'Serão necessárias {latas_tinta} latas de tinta. Valor total da compra: R${valor_compra:.2f},00.')