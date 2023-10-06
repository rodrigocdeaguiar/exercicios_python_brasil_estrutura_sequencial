area_pintada = (input('Digite a área a ser pintada, em m2: '))
area_pintadaTolerancia = float(area_pintada) + (float(area_pintada)*0.1)

cobertura_lata_tinta_pequena = 3.6*6
preco_lata_tinta_pequena = 25
cobertura_lata_tinta_grande = 18*6
preco_lata_tinta_grande = 80

if float(area_pintadaTolerancia) < cobertura_lata_tinta_pequena:
    qtde_latas_pequenas = 1
    valor_compra1 = preco_lata_tinta_pequena
elif float(area_pintadaTolerancia) > cobertura_lata_tinta_pequena:
    qtde_latas_pequenas = int(((float(area_pintadaTolerancia))/cobertura_lata_tinta_pequena)+1)
    valor_compra1 = preco_lata_tinta_pequena*qtde_latas_pequenas

print(f'Compra em latas pequenas:\n'
      f'Será(ão) necessária(s) {qtde_latas_pequenas} lata(s) pequena(s). Valor total: R${valor_compra1:.2f}.')

if float(area_pintadaTolerancia) < cobertura_lata_tinta_grande:
    qtde_latas_grandes = 1
    valor_compra2 = preco_lata_tinta_grande
elif float(area_pintadaTolerancia) > cobertura_lata_tinta_pequena:
    qtde_latas_grandes = int(((float(area_pintadaTolerancia))/cobertura_lata_tinta_grande)+1)
    valor_compra2 = preco_lata_tinta_grande*qtde_latas_grandes

print(f'Compra em latas grandes:\n'
      f'Será(ão) necessária(s) {qtde_latas_grandes} lata(s) grande(s). Valor total: R${valor_compra2:.2f}.')

if float(area_pintadaTolerancia) < cobertura_lata_tinta_grande:
    qtde_latas_pequenas_seg_opc = int(((float(area_pintadaTolerancia))/cobertura_lata_tinta_pequena)+1)
    valor_compra3 = preco_lata_tinta_pequena*qtde_latas_pequenas_seg_opc
    print(f'Compra em latas pequenas e grandes:\n'
     f'Será(ão) necessária(s) apenas {qtde_latas_pequenas_seg_opc} lata(s) pequena(s). Valor total: R${valor_compra3:.2f}.')
else:
    qtde_latas_grandes_seg_opc = (float(area_pintadaTolerancia) - (float(area_pintadaTolerancia)%cobertura_lata_tinta_grande))/cobertura_lata_tinta_grande
    qtde_latas_pequenas_seg_opc = int((float(float(area_pintadaTolerancia)%cobertura_lata_tinta_grande))/cobertura_lata_tinta_pequena + 1)
    valor_compra3 = (qtde_latas_pequenas_seg_opc*preco_lata_tinta_pequena) + (qtde_latas_grandes_seg_opc*preco_lata_tinta_grande)
    print(f'Compra em latas pequenas e grandes:\n'
          f'Será(ão) necessária(s) {qtde_latas_pequenas_seg_opc} lata(s) pequena(s) e {qtde_latas_grandes_seg_opc:.0f} lata(s) grande(s). Valor total: R${valor_compra3:.2f}.')