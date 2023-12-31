#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def inserir_produto_db(valor, nome, categoria): #FINALIZADO
    db.cur.execute("""
                   INSERT INTO produtos (VALOR, NOME, CATEGORIA) 
                   VALUES ('%s', '%s', '%s')
                   """ % (valor, nome, categoria))
    db.con.commit()
    
#função para inserir registro no banco de dados
def consultar_produto_db(): #FINALIZADO - PEDRO
    db.cur.execute("""
                   SELECT * FROM produtos
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

#função para  atualizar 
def atualizar_produto_db(id_produto, novo_valor, novo_nome, nova_categoria): #FINALIZADO - JOÃO E JEAN
    db.cur.execute("""
                    UPDATE produtos
                    SET valor = %s, nome = %s, categoria = %s 
                    WHERE id_produto = %s
                    """, (novo_valor, novo_nome, nova_categoria, id_produto))
    db.con.commit()

#função para deletar
def deletar_produto_db(id_produto): #FINALIZADO - ANA
    db.cur.execute("""
            DELETE from produtos
            WHERE id_produto = '%s'
            """ % (id_produto)
    )
    db.con.commit()