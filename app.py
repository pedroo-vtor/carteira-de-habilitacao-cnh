from flask import Flask, request, jsonify
import service
from model import Tarefa

app = Flask(__name__)

@app.route("/")
def ping():
    return "pig"

if __name__ == "__main__":
    app.run(debug=True, port=5000)