#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir_venda(data_venda, id_produto, cnpj, cpf_cliente): #FINALIZADO
    db.cur.execute("""
                   INSERT INTO vendas (DATA_VENDA, ID_PRODUTO, CNPJ, CPF_CLIENTE) 
                   VALUES ('%s', '%s', '%s', '%s')
                   """ % (data_venda, id_produto, cnpj, cpf_cliente))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar_venda(): #FINALIZADO - PEDRO
    db.cur.execute("""
                   SELECT * FROM vendas
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

#função para  atualizar 
def atualizar_venda(cpf, nome, endereco, telefone): #INACABADO - JOÃO E JEAN
    data = db.cur.execute("""
            UPDATE clientes SET cpf='%s', nome='%s', endereco='%s', telefone='%s'
            """ % (cpf, nome, endereco, telefone)
    )

#função para deletar
def deletar_venda(cpf, nome, endereco, telefone): #INACABADO - ANA
    data = db.cur.execute("""
            UPDATE clientes SET cpf='%s', nome='%s', endereco='%s', telefone='%s'
            """ % (cpf, nome, endereco, telefone)
    )