tamanhoArquivo = input('Digite o tamanho do arquivo que você fará o Download, em MB: ')
velocidadeInternet = input('Digite a velocidade da sua internet, em Mbps: ')

tempoDownload = float(tamanhoArquivo) / (float(velocidadeInternet)*60)

print(f'Seu arquivo de {tamanhoArquivo} MB, em uma intenet com velocidade {velocidadeInternet} Mbps, leverá {tempoDownload:.2f} min para ser baixado.')