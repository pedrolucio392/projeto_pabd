#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def inserir_cliente_db(cpf, nome, endereco, telefone): #FINALIZADO
    db.cur.execute("""
                   INSERT into public.clientes(CPF, NOME, ENDERECO, TELEFONE)
                   VALUES ('%s','%s','%s', '%s')
                   """ % (cpf, nome, endereco, telefone))
    db.con.commit()
    
#função para inserir registro no banco de dados
def consultar_cliente_db(): # FINALIZADO - PEDRO
    db.cur.execute("""
                   SELECT cpf, nome, endereco, telefone FROM clientes
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

#função para  atualizar 
def atualizar_cliente_db(cpf, nome, endereco, telefone): #INACABADO - JOÃO E JEAN
    db.cur.execute("""
            UPDATE clientes SET cpf='%s', nome='%s', endereco='%s', telefone='%s'
            """ % (cpf, nome, endereco, telefone)
    )
    db.con.commit()
    
#função para deletar
def deletar_cliente_db(cpf): #FINALIZADO - ANA
    db.cur.execute("""
            DELETE from clientes 
            WHERE cpf = '%s'
            """ % (cpf)
    )
    db.con.commit()