import csv

estado = input('Digite a sigla do estado desejado:')
estado = estado.upper()

#Transformar o TXT em CSV
with open(f"consulta_cand_2016_{estado}.txt", "r") as f:
    content = f.readlines()

with open(f"consulta_cand_2016_{estado}.csv", "w+") as csvfile:
    csvfile.writelines(content)
csvfile.close()    

#Abrindo e lendo o arquivo csv com o nome e código dos candidatos
lista_nomes = open(f'consulta_cand_2016_{estado}.csv', encoding='latin1')
leitor_nomes = csv.reader(lista_nomes, delimiter = ';')



#print(next(leitor_nomes))

#Limpando e pegando só as informações necessárias do arquivo

arquivo_saida = open(f'saidacandidatos{estado}.csv', mode='w', encoding='latin1')
escritor = csv.writer(arquivo_saida, lineterminator='\n')
escritor.writerow(['Ano', 'Cargo', 'Nome', 'Codigo', 'Situacao'])
for registro in leitor_nomes:
    escritor.writerow([registro[2], registro[7], registro[9], registro[10], registro[20], registro[-2]])
arquivo_saida.close()

