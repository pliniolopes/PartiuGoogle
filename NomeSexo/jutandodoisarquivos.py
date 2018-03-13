import csv
import pandas as pd

arquivo_bruto = open('nomes_bruto.csv', encoding='utf8')
leitor_bruto = csv.reader(arquivo_bruto)


arquivo_sexo = open('nomes_com_frequencia_ibge.csv', encoding='utf8')
leitor_sexo = csv.reader(arquivo_sexo)


#Ler arquivos com o pandas

leitor_bruto_pandas = pd.read_csv('names.csv', encoding='utf8', delimiter=';')
leitor_sexo_pandas = pd.read_csv('nomes_com_frequencia_ibge.csv', encoding='utf8', delimiter=';')

#Juntar os dois arquivos em um só com correspondencia pelo nome
juntar_leitor = pd.merge(leitor_bruto_pandas, leitor_sexo_pandas, on='name')

juntar_leitor.to_csv('tabelafinal.csv')
