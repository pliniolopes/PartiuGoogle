import csv


arquivo = open('nomes_bruto.csv', encoding='utf8')
leitor = csv.DictReader(arquivo, delimiter = ';')

arquivosaida = open('resultado.csv', mode='w', encoding='utf8')
escritor = csv.writer(arquivosaida, lineterminator='\n')




for registro in leitor:
    if registro['frequency_female'] > registro['frequency_male']:
        escritor.writerow([registro['name'], 'Feminino', registro['frequency_female'], registro ['frequency_male']])
    else:
        escritor.writerow([registro['name'], 'Masculino', registro['frequency_female'], registro ['frequency_male']])


arquivosaida.close()



