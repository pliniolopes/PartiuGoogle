import csv

lista_bens = open('bem_candidato_2016_PR.csv', encoding='latin1')
leitor_bens = csv.reader(lista_bens)


arquivo_saida = open('saidabens.csv', mode='w', encoding='utf8')
escritor =  csv.writer(arquivo_saida, lineterminator='\n')
escritor.writerow(['Ano', 'Codigo', 'Tipo', 'Descricao', 'Valor'])

for registro in leitor_bens:
    escritor.writerow([registro[2], registro[5], registro[7], registro[8], registro[9]])
arquivo_saida.close()
