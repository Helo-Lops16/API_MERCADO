import os

# # Caminho do arquivo CSV de produtos
file_path = 'produtos.csv'

# # Verificar se o arquivo CSV existe, se não existir cria 
if not os.path.exists(file_path):
#     # Criar um arquivo vazio 
     with open(file_path, mode='w', newline='', encoding='utf-8') as file:
#         # Escrevendo o cabeçalho do arquivo CSV
        file.write("ID,Nome,Fornecedor,Quantidade\n")
        print(f"O arquivo {file_path} foi criado com sucesso!")
else:
     print(f"O arquivo {file_path} já existe!")


#Escrevendo no arquivo produtos
import csv


# Dados a serem escritos no arquivo CSV
data = [
    ['ID', 'Nome', 'Fornecedor', 'Quantidade'],  
    [1, 'Arroz', 'Fornecedor A', 100],           
    [2, 'Feijão', 'Fornecedor B', 150],          
    [3, 'Macarrão', 'Fornecedor C', 200],        
    [4, 'Óleo', 'Fornecedor D', 50],             
    [5, 'Açúcar', 'Fornecedor E', 75]           
]

# Caminho para o arquivo CSV
file_path = 'produtos.csv'


# Abrir e escrever no arquivo CSV
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Escreve todas as linhas



