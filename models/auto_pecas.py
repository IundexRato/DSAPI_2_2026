from config.conexao import get_connection
class AutoPecasModel:
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, nome, categoria, marca, preco FROM produtos")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def insert(dados):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO produtos (nome, categoria, marca, preco) VALUES (%s, %s, %s, %s)"
        valores = (dados.get('nome'), dados.get('categoria'), dados.get('marca'), dados.get('preco'))
        cursor.execute(sql, valores)
        conn.commit()
        last_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return last_id

    @staticmethod
    def update(peca_id, dados):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "UPDATE produtos SET nome=%s, categoria=%s, marca=%s, preco=%s WHERE id=%s"
        valores = (dados.get('nome'), dados.get('categoria'), dados.get('marca'), dados.get('preco'), peca_id)
        cursor.execute(sql, valores)
        conn.commit()
        rowcount = cursor.rowcount
        cursor.close()
        conn.close()
        return rowcount

    @staticmethod
    def delete(peca_id):
        conn = get_connection()
        cursor = conn.cursor()
        sql = ("DELETE FROM produtos WHERE id = %s")
        valores = (peca_id,)
        cursor.execute(sql, valores)
        conn.commit()
        rowcount = cursor.rowcount
        cursor.close()
        conn.close()
        return rowcount > 0
