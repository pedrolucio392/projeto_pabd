import streamlit as st
import controller.cliente as cliente

# ANA -FINALIZADO(EXCETO VENDA - PK)

def deletar_cliente(cpf):
    db.cur.execute("""
            delete from clientes where cpf= '%s'
"""%(cpf))
    db.cur.commit()

def deletar_produto(id):
    db.cur.execute("""
            delete from produto where id= '%s'
"""%(id))
    db.cur.commit()

def deletar_supermercado(cnpj):
    db.cur.execute("""
            delete from supermercado where cnpj= '%s'
"""%(cnpj))
    db.cur.commit()

def deletar_venda(): 
    db.cur.execute("""
            delete from venda where = '%s'
"""%())
    db.cur.commit()
