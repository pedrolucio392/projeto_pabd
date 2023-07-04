#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(cpf, nome, endereco, telefone):
    db.cur.execute("""
                   INSERT into public.tb_cliente (cpf, nome, endereco, telefone)
                   VALUES ('%s','%s','%s', '%s')
                   """ % (cpf, nome, endereco, telefone))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM public.tb_cliente
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

#função para  atualizar 
def atualizar_cliente(cpf, nome, endereco, telefone):
    data = db.cur.execute("""
            UPDATE clientes SET cpf='%s', nome='%s', endereco='%s', telefone='%s'
            """ % (cpf, nome, endereco, telefone)
    )