from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

# Caminhos dos arquivos CSV = Transformados em variáveis
CLIENTES_CSV = "clientes.csv"
PRODUTOS_CSV = "produtos.csv"
ORDENS_CSV = "ordens.csv"

#Executa leitura do arquivo
def ler_csv(arquivo):
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

#Executa escrita do arquivo
def escrever_csv(arquivo, dados, campos):
    with open(arquivo, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(dados)

#------------------#

# Clientes 

#Retorna as informações dos clientes
@app.route('/clientes', methods=['GET']) #ok
def listar_clientes():
    return jsonify(ler_csv(CLIENTES_CSV))

#Te permite adicionar um novo cliente
@app.route('/add_clientes', methods=['POST']) #ok
def adicionar_cliente():
    clientes = ler_csv(CLIENTES_CSV)
    novo_id = max([int(c["ID"]) for c in clientes], default=0) + 1
    novo_cliente = {
        "ID": str(novo_id),
        "Nome": request.json["Nome"],
        "Sobrenome": request.json["Sobrenome"],
        "Data de nascimento": request.json["Data de nascimento"],
        "CPF": request.json["CPF"]
    }
    clientes.append(novo_cliente)
    escrever_csv(CLIENTES_CSV, clientes, novo_cliente.keys())
    return jsonify(novo_cliente), 201

#Atualiza as infor
@app.route('/up_clientes/<id>', methods=['PUT']) #ok colocar na doc q deve passar up_clientes / o id
def atualizar_cliente(id):
    clientes = ler_csv(CLIENTES_CSV)

    id_str = str(id)

    for cliente in clientes:
        if str(cliente["ID"]) == id_str:
            if not request.json:
                return jsonify({"error": "Nenhum dado enviado"}), 400
            
            cliente.update(request.json)
            escrever_csv(CLIENTES_CSV, clientes, cliente.keys())
            return jsonify(cliente), 200

    return jsonify({"error": "Cliente não encontrado"}), 404

@app.route('/del_clientes/<id>', methods=['DELETE']) #ok colocar na doc q deve passar del_clientes / o id
def remover_cliente(id):
    clientes = ler_csv(CLIENTES_CSV)
    clientes = [c for c in clientes if c["ID"] != id]
    escrever_csv(CLIENTES_CSV, clientes, ["ID", "Nome", "Sobrenome", "Data de nascimento", "CPF"])
    return jsonify({"message": "Cliente removido"}), 200

#------------------#

# Produtos 
@app.route('/produtos', methods=['GET']) #ok
def listar_produtos():
    return jsonify(ler_csv(PRODUTOS_CSV))

@app.route('/add_produtos', methods=['POST']) #ok
def adicionar_produto():
    produtos = ler_csv(PRODUTOS_CSV)
    novo_id = max([int(p["ID"]) for p in produtos], default=0) + 1
    novo_produto = {
        "ID": str(novo_id),
        "Nome": request.json["Nome"],
        "Fornecedor": request.json["Fornecedor"],
        "Quantidade": int(request.json["Quantidade"])
    }
    produtos.append(novo_produto)
    escrever_csv(PRODUTOS_CSV, produtos, novo_produto.keys())
    return jsonify(novo_produto), 201

@app.route('/up_produtos/<id>', methods=['PUT']) #ok
def atualizar_produto(id):
    produtos = ler_csv(PRODUTOS_CSV)
    for produto in produtos:
        if produto["ID"] == id:
            produto.update(request.json)
            escrever_csv(PRODUTOS_CSV, produtos, produto.keys())
            return jsonify(produto), 200
    return jsonify({"error": "Produto não encontrado"}), 404

@app.route('/del_produtos/<id>', methods=['DELETE']) #ok
def remover_produto(id):
    produtos = ler_csv(PRODUTOS_CSV)
    produtos = [p for p in produtos if p["ID"] != id]
    escrever_csv(PRODUTOS_CSV, produtos, ["ID", "Nome", "Fornecedor", "Quantidade"])
    return jsonify({"message": "Produto removido"}), 200

#------------------#

# Ordens de Venda 
@app.route('/ordens', methods=['GET']) #ok
def listar_ordens():
    return jsonify(ler_csv(ORDENS_CSV))

@app.route('/add_ordens', methods=['POST']) #ok
def criar_ordem():
    ordens = ler_csv(ORDENS_CSV)
    novo_id = max([int(o["ID_O"]) for o in ordens], default=0) + 1

    data = request.get_json()  # Obtém o JSON corretamente

    if not data:
        return jsonify({"erro": "Requisição não contém um JSON válido"}), 400

    cliente = data.get("Cliente")
    produto = data.get("Produto")

    if not cliente or not produto:
        return jsonify({"erro": "Campos 'Cliente' e 'Produto' são obrigatórios"}), 400

    nova_ordem = {
        "ID_O": novo_id,
        "Cliente": cliente,
        "Produto": produto
    }

    ordens.append(nova_ordem)
    escrever_csv(ORDENS_CSV, ordens, nova_ordem.keys())

    return jsonify(nova_ordem), 201


@app.route('/up_ordens/<id>', methods=['PUT']) #ok
def atualizar_ordem(id):
    ordens = ler_csv(ORDENS_CSV)
    for ordem in ordens:
        if ordem["ID_O"] == id:
            ordem.update(request.json)
            escrever_csv(ORDENS_CSV, ordens, ordem.keys())
            return jsonify(ordem), 200
    return jsonify({"error": "Ordem não encontrada"}), 404

@app.route('/del_ordens/<id>', methods=['DELETE']) #ok
def remover_ordem(id):
    ordens = ler_csv(ORDENS_CSV)

    # Filtra ordens e verifica se alguma foi removida
    novas_ordens = [o for o in ordens if str(o["ID_O"]) != str(id)]

    if len(novas_ordens) == len(ordens):  # Se nenhuma ordem foi removida
        return jsonify({"error": "Ordem não encontrada"}), 404

    escrever_csv(ORDENS_CSV, novas_ordens, ["ID_O", "Cliente", "Produto"])
    return jsonify({"message": "Ordem removida"}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)