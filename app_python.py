from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados simulados (em um projeto real, viriam de um banco de dados)
usuarios_db = [
    {"id": 1, "nome": "Alice", "email": "alice@example.com"},
    {"id": 2, "nome": "Bob", "email": "bob@example.com"}
]
produtos_db = [
    {"id": 101, "sku": "PRD001", "nome": "Notebook", "preco": 3500.00},
    {"id": 102, "sku": "PRD002", "nome": "Mouse", "preco": 80.00}
]
pedidos_db = {
    1001: {"id": 1001, "usuario_id": 1, "produto_id": 101, "quantidade": 1, "status": "Processando"},
    1002: {"id": 1002, "usuario_id": 2, "produto_id": 102, "quantidade": 2, "status": "Concluído"}
}
estoque_db = {
    101: 50, # Notebook
    102: 120 # Mouse
}

# --- Endpoints de Dados ---
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios_db)

@app.route('/usuarios', methods=['POST'])
def create_usuario():
    novo_usuario = request.json
    if not novo_usuario or 'nome' not in novo_usuario or 'email' not in novo_usuario:
        return jsonify({"erro": "Dados incompletos para o usuário"}), 400
    novo_usuario['id'] = len(usuarios_db) + 1
    usuarios_db.append(novo_usuario)
    return jsonify(novo_usuario), 201

@app.route('/produtos', methods=['GET'])
def get_produtos():
    return jsonify(produtos_db)

@app.route('/pedidos/<int:pedido_id>', methods=['GET'])
def get_pedido(pedido_id):
    pedido = pedidos_db.get(pedido_id)
    if pedido:
        return jsonify(pedido)
    return jsonify({"erro": "Pedido não encontrado"}), 404

@app.route('/estoque/<int:produto_id>', methods=['PUT'])
def update_estoque(produto_id):
    data = request.json
    if 'quantidade' not in data or not isinstance(data['quantidade'], int):
        return jsonify({"erro": "Quantidade inválida"}), 400

    if produto_id in estoque_db:
        estoque_db[produto_id] = data['quantidade']
        return jsonify({"mensagem": f"Estoque do produto {produto_id} atualizado para {data['quantidade']}", "novo_estoque": estoque_db[produto_id]})
    return jsonify({"erro": "Produto não encontrado no estoque"}), 404

# --- Endpoints de Validação ---
@app.route('/validar/usuario/<int:usuario_id>', methods=['GET'])
def validar_usuario(usuario_id):
    usuario_existe = any(u['id'] == usuario_id for u in usuarios_db)
    if usuario_existe:
        return jsonify({"valido": True, "mensagem": f"Usuário {usuario_id} é válido"})
    return jsonify({"valido": False, "mensagem": f"Usuário {usuario_id} não encontrado"}), 404

@app.route('/validar/produto/<string:sku>', methods=['GET'])
def validar_produto(sku):
    produto_existe = any(p['sku'] == sku for p in produtos_db)
    if produto_existe:
        return jsonify({"valido": True, "mensagem": f"Produto com SKU {sku} é válido"})
    return jsonify({"valido": False, "mensagem": f"Produto com SKU {sku} não encontrado"}), 404

@app.route('/validar/documento', methods=['POST'])
def validar_documento():
    data = request.json
    documento = data.get('numero')
    tipo = data.get('tipo')

    if not documento or not tipo:
        return jsonify({"valido": False, "mensagem": "Documento ou tipo não fornecidos"}), 400

    # Simulação de validação (em um caso real, teria lógica de validação de CPF/CNPJ)
    if tipo == "CPF" and len(documento) == 11 and documento.isdigit():
        return jsonify({"valido": True, "mensagem": f"CPF {documento} é válido (formato)"})
    elif tipo == "CNPJ" and len(documento) == 14 and documento.isdigit():
        return jsonify({"valido": True, "mensagem": f"CNPJ {documento} é válido (formato)"})
    else:
        return jsonify({"valido": False, "mensagem": f"Documento {documento} tipo {tipo} inválido"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000) # Rodará na porta 5000