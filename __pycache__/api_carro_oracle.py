from flask import Flask, request, jsonify
import db_oracle

app = Flask(__name__)

@app.route("/veiculos", methods=['POST'])
def inclui_carro():
    carro = request.json
    try:
        db_oracle.insert_carro(carro)
        return carro, 201
    except Exception as erro:
        print(erro)
        info = {"msg": "Carro não cadastrado"}
        return info, 404

app.run(debug=True)