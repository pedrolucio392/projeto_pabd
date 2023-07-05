#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir_supermercado(cnpj, nome_supermercado, proprietario): #FINALIZADO
    db.cur.execute("""
                   INSERT INTO supermercados (CNPJ, NOME_SUPERMERCADO, PROPRIETARIO) 
                   VALUES ('%s', '%s', '%s')
                   """ % (cnpj, nome_supermercado, proprietario))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar_supermercado(): #FINALIZADO - PEDRO
    db.cur.execute("""
                   SELECT * FROM supermercados
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

#função para  atualizar 
def atualizar_supermercado(cpf, nome, endereco, telefone): #INACABADO - JOÃO E JEAN
    data = db.cur.execute("""
            UPDATE clientes SET cpf='%s', nome='%s', endereco='%s', telefone='%s'
            """ % (cpf, nome, endereco, telefone)
    )

#função para deletar
def deletar_supermercado(cnpj): #FINALIZADO - ANA
    data = db.cur.execute("""
            UPDATE clientes SET cnpj='%s'
            """ % (cnpj)
    )