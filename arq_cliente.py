import os

# #Criação dos arquivos csv dos clientes

# # # Caminho do arquivo CSV de clientes
# file_path = 'clientes.csv'

# # # Verificar se o arquivo CSV existe, se não existir cria.
# if not os.path.exists(file_path):
# #     # Criar um arquivo vazio
#      with open(file_path, mode='w', newline='', encoding='utf-8') as file:
# #         # Escrevendo o cabeçalho do arquivo CSV
#         file.write("ID,Nome,Sobrenome,Data de nascimento,CPF\n")
#      print(f"O arquivo {file_path} foi criado com sucesso!")
# else:
#      print(f"O arquivo {file_path} já existe!")


# #Escrevendo no arquivo clientes
import csv

# # Dados a serem escritos no arquivo CSV
data = [
     ['ID', 'Nome', 'Sobrenome', 'Data de nascimento', 'CPF'],  
     [1, 'Evandro', 'Martins', '1990-01-01', '12345678901'],  
     [2, 'Ullian', 'Pirana', '2008-01-13', '98765432100'] ,
     [3, 'Amir', 'Pereira', '1941-03-15', '11223344556'],  
     [4, 'Maisa', 'Abravanel', '2002-07-22', '22334455667'],       
     [5, 'Roberto', 'Almeida', '1978-09-30', '33445566778'] 
]

# # Caminho para o arquivo CSV
file_path = 'clientes.csv'

# # Abrir e escrever no arquivo CSV
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
     writer = csv.writer(file)
     writer.writerows(data)  # Escreve todas as linhas