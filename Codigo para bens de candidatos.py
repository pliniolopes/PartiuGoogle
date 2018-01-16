import csv

estado = input('Digite a sigla do estado desejado:')
estado = estado.upper()

#Transformar o TXT em CSV
with open(f"bem_candidato_2016_{estado}.txt", "r") as f:
    content = f.readlines()

with open(f"bem_candidato_2016_{estado}.csv", "w+") as csvfile:
    csvfile.writelines(content)
csvfile.close()  

#Abrindo e lendo o arquivo csv com o código e os bens dos candidatos
lista_bens = open(f'bem_candidato_2016_{estado}.csv', encoding='latin1')
leitor_bens = csv.reader(lista_bens, delimiter = ';')


#Limpando e pegando só as informações necessárias do arquivo
#print(next(leitor_nomes))


arquivo_saida = open(f'saidabens{estado}.csv', mode='w', encoding='latin1')
escritor =  csv.writer(arquivo_saida, lineterminator='\n')
escritor.writerow(['Ano', 'Codigo', 'Tipo', 'Descricao', 'Valor'])


for registro in leitor_bens:
    escritor.writerow([registro[2], registro[5], registro[7], registro[8], registro[9]])
arquivo_saida.close()
