get_all_spec = {
    "responses": {
        "200": {
            "description": "Lista de produtos retornada com sucesso",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "nome": {"type": "string"},
                        "categoria": {"type": "string"},
                        "marca": {"type": "string"},
                        "preco": {"type": "float"}
                    }
                }
            }
        }
    }
}

insert_spec = {
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "nome": {"type": "string"},
                    "categoria": {"type": "string"},
                    "marca": {"type": "string"},
                    "preco": {"type": "number"}
                }
            }
        }
    ],
    "responses": {
        "201": {"description": "Produto cadastrado com sucesso"}
    }
}

update_spec = {
    "parameters": [
        {
            "name": "produto_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do produto"
        },
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "nome": {"type": "string"},
                    "categoria": {"type": "string"},
                    "marca": {"type": "string"},
                    "preco": {"type": "number"}
                }
            }
        }
    ],
    "responses": {
        "200": {"description": "Produto atualizado com sucesso"},
        "404": {"description": "Produto não encontrado"}
    }
}

delete_spec = {
    "parameters": [
        {
            "name": "produto_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do produto"
        }
    ],
    "responses": {
        "200": {"description": "Produto removido com sucesso"},
        "404": {"description": "Produto não encontrado"}
    }
}
