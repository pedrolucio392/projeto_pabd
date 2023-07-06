#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def inserir_supermercado_db(cnpj, nome_supermercado, proprietario): #FINALIZADO
    db.cur.execute("""
                   INSERT INTO supermercados (CNPJ, NOME_SUPERMERCADO, PROPRIETARIO) 
                   VALUES ('%s', '%s', '%s')
                   """ % (cnpj, nome_supermercado, proprietario))
    db.con.commit()
    
#função para inserir registro no banco de dados
def consultar_supermercado_db(): #FINALIZADO - PEDRO
    db.cur.execute("""
                   SELECT * FROM supermercados
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

#função para  atualizar 
def atualizar_supermercado_db(cpf, nome, endereco, telefone): #INACABADO - JOÃO E JEAN
    data = db.cur.execute("""
            UPDATE clientes SET cpf='%s', nome='%s', endereco='%s', telefone='%s'
            """ % (cpf, nome, endereco, telefone)
    )

#função para deletar
def deletar_supermercado_db(cnpj): #FINALIZADO - ANA
    db.cur.execute("""
            DELETE from supermercados
            WHERE cnpj = '%s'
            """ % (cnpj)
    )
    db.con.commit()