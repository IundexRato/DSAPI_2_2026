from flask import Flask, request
from flasgger import Swagger, swag_from
from controllers.auto_pecas_controller import AutoPecasController
from config.swagger import(
    get_all_spec,
    insert_spec,
    update_spec,
    delete_spec
)

app = Flask(__name__)

swagger_config = {
    "headers": [],
    "specs": [
    {
        "endpoint": 'apispec_1',
        "route": '/apispec_1.json',
        "rule_filter": lambda rule: True,
        "model_filter": lambda rule: True,
    }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/produtos/swagger"
}

swagger = Swagger(app, config=swagger_config)

@app.route('/produtos', methods=['GET'])
@swag_from(get_all_spec)
def listar_todas():
    return AutoPecasController.mostrar_tudo()

@app.route('/produtos/', methods=['POST'])
@swag_from(insert_spec)
def cadastrar_serie():
    dados = request.json
    return AutoPecasController.cadastrar(dados)

@app.route('/produtos/<int:produto_id>', methods=['PUT'])
@swag_from(update_spec)
def atualizar_serie(produto_id):
    dados = request.json
    return AutoPecasController.atualizar(produto_id, dados)

@app.route('/produtos/<int:produto_id>', methods=['DELETE'])
@swag_from(delete_spec)
def excluir_serie(produto_id):
    return AutoPecasController.excluir(produto_id)

if __name__ == '__main__':
    app.run(debug=True)
