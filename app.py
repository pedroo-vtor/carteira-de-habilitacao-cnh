# app.py
from flask import Flask, jsonify, request, abort
from database import init_db, deletar_tabela_temporariamente
from model import (
    listar_carteiras,
    obter_carteira_por_id,
    criar_carteira,
    atualizar_carteira,
    deletar_carteira,
    Carteira,
)

app = Flask(__name__)

initialized = False

@app.before_request
def inicializar_banco():
    init_db()
    initialized = True

#Função para deletar a tabela (caso necessário)
#@app.route("/", methods=["GET"])
#def criar_bd():
#    deletar_tabela_temporariamente()
#    return 'Banco deletado!'

#Criar Carteira (CREATE)
@app.route("/carteiras", methods=["POST"])
def rota_criar_carteira():
    dados = request.get_json() or {}

    nome = dados.get("nome")
    sobrenome = dados.get("sobrenome")
    cpf = dados.get("cpf")
    nacionalidade = dados.get("nacionalidade")
    categoria = dados.get("categoria")
    data_emissao = dados.get("data_emissao") # string 'YYYY-MM-DD' ou None
    validade = dados.get("validade")   # string 'YYYY-MM-DD' ou None

    carteira = criar_carteira(nome, sobrenome, cpf, nacionalidade, categoria, data_emissao, validade)
    return jsonify(carteira.to_dict()), 201

# Listar todas as carteiras (READ)
@app.route("/carteiras", methods=["GET"])
def rota_listar_carteiras():
    carteiras = listar_carteiras()
    return jsonify([t.to_dict() for t in carteiras]), 200

# Obter Carteira por ID (READ)
@app.route("/carteiras/<int:id_carteira>", methods=["GET"])
def rota_obter_carteira(id_carteira):
    carteira = obter_carteira_por_id(id_carteira)
    if not carteira:
        abort(404, description="Carteira não encontrada.")
    return jsonify(carteira.to_dict()), 200

# Atualizar Carteira (UPDATE)
@app.route("/carteiras/<int:id_carteira>", methods=["PUT"])
def rota_atualizar_carteira(id_carteira):
    carteira = obter_carteira_por_id(id_carteira)
    if not carteira:
        abort(404, description="Carteira não encontrada.")

    dados = request.get_json() or {}

    if "nome" in dados:
        carteira.nome = dados["nome"]
    if "sobrenome" in dados:
        carteira.sobrenome = dados["sobrenome"]
    if "cpf" in dados:
        carteira.cpf = dados["cpf"]
    if "nacionalidade" in dados:
        carteira.nacionalidade = dados["nacionalidade"]
    if "categoria" in dados:
        carteira.categoria = dados["categoria"]
    if "data_emissao" in dados:
        carteira.data_emissao = dados["data_emissao"]
    if "validade" in dados:
        carteira.validade = dados["validade"]

    carteira = atualizar_carteira(carteira)
    return jsonify(carteira.to_dict()), 200

#DELETE Carteira
@app.route("/carteiras/<int:id_carteira>", methods=["DELETE"])
def rotar_deletar_carteira(id_carteira):
    ok = deletar_carteira(id_carteira)
    if not ok:
        abort(404, description="Carteira não encontrada.")
    return jsonify({"mensagem": "Carteira removida com sucesso."}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)