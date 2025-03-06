import os

# # Caminho do arquivo CSV de c
file_path = 'ordem_vendas.csv'

# # Verificar se o arquivo CSV existe, se não existir cria o mesmo
if not os.path.exists(file_path):
#     # Criar um arquivo vazio e adicionar o cabeçalho
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
#         # Escrevendo o cabeçalho do arquivo CSV
       file.write("ID_O,Cliente, Produto\n")
       print(f"O arquivo {file_path} foi criado com sucesso!")
else:
    print(f"O arquivo {file_path} já existe!")


#Escrevendo no arquivo ordem de vendas
import csv


# Dados a serem escritos no arquivo CSV
data = [
    ['ID_O', 'Cliente', 'Produto'],  
    [1,2,2],  
    [4,4,3],
    [2,3,5], 
    [5,1,1],
    [3,2,4]
]

# Caminho para o arquivo CSV
file_path = 'ordem_vendas.csv'


# Abrir e escrever no arquivo CSV
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Escreve todas as linhas

