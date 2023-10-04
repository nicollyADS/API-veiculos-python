from flask import Flask, request, jsonify
import db_oracle
import traceback

app = Flask(__name__)

@app.route("/veiculos", methods=['GET'])
def recupera_carros():
    try:
        dado = db_oracle.consulta_todos()
        list_dic = []
        for reg in dado:
            # carro = {"id":reg[0], "ano":[1], "montadora":[2],... }
            carro = {}
            carro['id'] = reg[0]
            carro['ano'] = reg[1]
            carro['montadora'] = reg[2]
            carro['modelo'] = reg[3]
            carro['placa'] = reg[4]
            list_dic.append(carro)
        return list_dic, 200
    except Exception as erro:
        print("deu erro")
        info = {"msg": "Erro na consulta"}
        return info, 401
    


@app.route("/veiculos", methods=['POST'])
def inclui_carro():
    carro = request.json
    try:
        db_oracle.insert_carro(carro)
        return carro, 201
    except Exception as erro:
        traceback.print_exc()
        info = {"msg": "Carro não cadastrado"}
        return info, 404

app.run(debug=True)