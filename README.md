# Tutorial de Testes da API Supermercado com Postman

**Preparação**

Antes de começar os testes, **inicie a API** executando o seguinte comando no terminal:

```bash
bash
python nome_do_arquivo.py
```

Se sua API estiver rodando corretamente, o terminal mostrará algo como:

```bash
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Agora, abra o **Postman**.

---

## **Testando Clientes**

### **1. Listar todos os clientes**

**Método**: GET

**URL**: http://127.0.0.1:5000/clientes

**Clique em "Send"**

**Resposta esperada (exemplo)**:

### **2. Adicionar um novo cliente**

[](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

**Método**: POST

**URL**: http://127.0.0.1:5000/clientes

**Aba "Body"** → **Selecionar "raw"** → **Selecionar "JSON"**

**Inserir este JSON**:

```json
{
    "Nome": "",
    "Sobrenome": "",
    "Data de nascimento": "",
    "CPF": ""
}
```

*Substitua os valores dentro das aspas vazias pelos valores que deseja adicionar do cliente*

**Clique em "Send"**

**Resposta esperada:**

```json
{
    "ID": "id_do_cliente",
    "Nome": "nome_adicionado",
    "Sobrenome": "sobrenome_adicionado",
    "Data de nascimento": "datadenascimento_adicionada",
    "CPF": "cpf_adicionado"
}
```

### **3. Atualizar um cliente existente**

[](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

**Método**: PUT

**URL**: http://127.0.0.1:5000/upd_clientes/id_do_cliente

**Aba "Body"** → **Selecionar "raw"** → **Selecionar "JSON"**

**Inserir este JSON**:

*Utilizando como exemplo:*

***URL**: http://127.0.0.1:5000/clientes/1*

```json
{
    "Nome": "Evandro Atualizado",
    "Sobrenome": "Martins",
    "Data de nascimento": "1990-01-01",
    "CPF": "12345678901"
}
```

**Clique em "Send"**

**Resposta esperada**:

```json
{
    "ID": "1",
    "Nome": "Evandro Atualizado",
    "Sobrenome": "Martins",
    "Data de nascimento": "1990-01-01",
    "CPF": "12345678901"
}
```

### **4. Remover um cliente**

[](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

**Método**: DELETE

**URL**: http://127.0.0.1:5000/del_clientes/id_do_cliente

**Clique em "Send"**

**Resposta esperada**:

*Exemplo:*

**URL**: http://127.0.0.1:5000/del_clientes/1

```json
{
    "message": "Cliente removido"
}
```

---

### **Testando Produtos**

### **1. Listar todos os produtos**

**Método**: GET

**URL**: http://127.0.0.1:5000/produtos

**Clique em "Send"**

**Resposta esperada**:

```json
{
        "ID": "id_dos_produtos",
        "Nome": "nomedoproduto",
        "Fornecedor": "fornecedordoproduto",
        "Quantidade": "quantidadedoproduto"
    }
```

### **2. Adicionar um novo produto**

[](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

**Método**: POST

**URL**: http://127.0.0.1:5000/add_produtos

**Aba "Body"** → **Selecionar "raw"** → **Selecionar "JSON"**

**Inserir este JSON**:

```json
{
    "Nome": "Farinha",
    "Fornecedor": "Fornecedor Z",
    "Quantidade": "50"
}
```

Lembrando que esse exemplo pode ser alterado para como deseja

**Clique em "Send"**

**Resposta esperada**:

```json
{
    "ID": "6",
    "Nome": "Farinha",
    "Fornecedor": "Fornecedor Z",
    "Quantidade": "50"
}
```

### **3. Atualizar um produto existente**

**Método**: PUT

**URL**: http://127.0.0.1:5000/upd_produtos/id_do_produto

**Aba "Body"** → **Selecionar "raw"** → **Selecionar "JSON"**

**Inserir este JSON**:

*Exemplo:*

***URL**: http://127.0.0.1:5000/upd_produtos/1*

```json
{
    "Nome": "Arroz Integral",
    "Fornecedor": "Fornecedor A",
    "Quantidade": "120"
}
```

**Clique em "Send"**

**Resposta esperada**:

```json
{
    "ID": "1",
    "Nome": "Arroz Integral",
    "Fornecedor": "Fornecedor A",
    "Quantidade": "120"
}
```

**4. Remover um produto**

**Método**: DELETE

**URL**: http://127.0.0.1:5000/del_produtos/id_do_produto

**Clique em "Send"**

**Resposta esperada**:

*Exemplo:*

***URL**: http://127.0.0.1:5000/del_produtos/6*

```json
{
    "message": "Produto removido"
}
```

---

### **Testando Ordens de Venda**

### **1. Listar todas as ordens de venda**

**Método**: GET

**URL**: http://127.0.0.1:5000/ordens

**Clique em "Send"**

**Resposta esperada**:

```json
{
        "ID_O": "1",
        "Cliente": "2",
        "Produto": "2"
    }
```

### **2. Criar uma nova ordem de venda**

**Método**: POST

**URL**: http://127.0.0.1:5000/add_ordens

**Aba "Body"** → **Selecionar "raw"** → **Selecionar "JSON"**

**Inserir este JSON**:

```json
{
    "Cliente": "3",
    "Produto": "5"
}
```

**Clique em "Send"**

**Resposta esperada**:

```json
{
    "ID_O": "6",
    "Cliente": "3",
    "Produto": "5"
}
```

### **3. Atualizar uma ordem de venda**

**Método**: PUT

**URL**: http://127.0.0.1:5000/upd_ordens/id_do_cliente

**Aba "Body"** → **Selecionar "raw"** → **Selecionar "JSON"**

**Inserir este JSON**:

*Exemplo:*

***URL**: http://127.0.0.1:5000/upd_ordens/1*

```json
{
    "Cliente": "4",
    "Produto": "1"
}
```

**Clique em "Send"**

**Resposta esperada**:

```json
{
    "ID_O": "1",
    "Cliente": "4",
    "Produto": "1"
}
```

**4. Remover uma ordem de venda**

**Método**: DELETE

**URL**: http://127.0.0.1:5000/del_ordens/id_do_cliente

**Clique em "Send"**

**Resposta esperada**:

```json
{
    "message": "Ordem removida"
}
```
