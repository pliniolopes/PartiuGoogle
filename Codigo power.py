import csv


#Abrindo e lendo o arquivo csv com o nome e código dos candidatos
lista_nomes = open('consulta_cand_2016_PR2.csv', encoding='utf8')
leitor_nomes = csv.reader(lista_nomes)



#Limpando e pegando só as informações necessárias do arquivo

arquivo_saida = open('saidacandidatos.csv', mode='w', encoding='utf8')
escritor = csv.writer(arquivo_saida, lineterminator='\n')
escritor.writerow(['Ano', 'Cargo', 'Nome', 'Codigo', 'Situacao'])
for registro in leitor_nomes:
    escritor.writerow([registro[2], registro[7], registro[9], registro[10], registro[20], registro[-2]])
arquivo_saida.close()

