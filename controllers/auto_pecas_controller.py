from flask import jsonify
from models.auto_pecas import AutoPecasModel

class AutoPecasController:
    @staticmethod
    def mostrar_tudo():
        produtos = AutoPecasModel.get_all()
        return jsonify(produtos)

    @staticmethod
    def cadastrar(dados):
        novo_id = AutoPecasModel.insert(dados)
        return jsonify({"mensagem": "Produto cadastrada com sucesso!", "id": novo_id}), 201

    @staticmethod
    def atualizar(produto_id, dados):
        sucesso = AutoPecasModel.update(produto_id, dados)
        if sucesso:
            return jsonify({"mensagem": "Produto atualizada com sucesso!"})
        return jsonify({"erro": "Produto não encontrada!"}), 404

    @staticmethod
    def excluir(produto_id):
        sucesso = AutoPecasModel.delete(produto_id)
        if sucesso:
            return jsonify({"mensagem": "Produto excluida com sucesso!"})
        return jsonify({"erro": "Produto não encontrada!"}), 404