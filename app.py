from flask import Flask, request, jsonify
import service
from model import Carteira

app = Flask(__name__)

#PING (Rota Raíz)
@app.route("/")
def ping():
    return "pig"

#CREATE
@app.route("/carteiras", methods=["POST"])
def criar_carteira():
    try:
        dados = request.get_json()
        mensagem_retorno = service.adicionar_carteira(dados)
        return jsonify(mensagem_retorno), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

#READ
@app.route("/carteiras", methods=["GET"])
def listar_carteiras():
    return jsonify(service.listar_carteiras())

#UPDATE
@app.route("/carteiras/<int:carteira_id>", methods=["PUT"])
def atualizar_carteira(carteira_id):
    try:
        dados = request.get_json()
        carteira = service.atualizar_carteira(carteira_id,dados)
        return jsonify(carteira)
    except IndexError as e:
        return jsonify({"erro": str(e)}), 400

#DELETE
@app.route("/carteiras/<int:carteira_id>", methods=["DELETE"])
def deletar_carteira(carteira_id):
    try:
        carteira = service.deletar_carteira(carteira_id)
        return jsonify({"mensagem": "Carteira removida com sucesso.", "carteira": carteira})
    except IndexError as e:
        return jsonify({"erro": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)