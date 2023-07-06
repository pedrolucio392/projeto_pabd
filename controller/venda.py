#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def inserir_venda_db(data_venda, id_produto, cnpj, cpf_cliente): #FINALIZADO
    db.cur.execute("""
                   INSERT INTO vendas (DATA_VENDA, ID_PRODUTO, CNPJ, CPF_CLIENTE) 
                   VALUES ('%s', '%s', '%s', '%s')
                   """ % (data_venda, id_produto, cnpj, cpf_cliente))
    db.con.commit()
    
#função para inserir registro no banco de dados
def consultar_venda_db(): #FINALIZADO - PEDRO
    db.cur.execute("""
                   SELECT * FROM vendas
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

#função para  atualizar 
def atualizar_venda_db(cpf, nome, endereco, telefone): #INACABADO - JOÃO E JEAN
    data = db.cur.execute("""
            UPDATE clientes SET cpf='%s', nome='%s', endereco='%s', telefone='%s'
            """ % (cpf, nome, endereco, telefone)
    )

#função para deletar
def deletar_venda_db(id_venda): #FINALIZADO - ANA
    db.cur.execute("""
            DELETE from vendas 
            WHERE id_venda = '%s'
            """ % (id_venda)
    )
    db.con.commit()