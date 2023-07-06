import streamlit as st
import services.database as db

import controller.cliente as cliente
import controller.produto as produto
import controller.supermercado as supermercado
import controller.venda as venda

from psycopg2.errors import ForeignKeyViolation


# ANA - FINALIZADO

def deletar_cliente():
    st.title('Deletar cliente')
    
    with st.form(key='delete_cliente'):
        input_cpf = st.number_input(label='Insira o CPF que deseja excluir:', format='%d', step=1)

        button_submit = st.form_submit_button('Deletar')

        if button_submit:
            try:
                cliente.deletar_cliente_db(input_cpf)
                st.success('Cliente deletado com sucesso')
            except ForeignKeyViolation:
                st.error('Cliente possui vendas cadastradas, exclua suas vendas antes de deletá-lo')
                db.con.rollback()
            
def deletar_produto():
    st.title('Deletar produto')
    
    with st.form(key='delete_produto'):
        input_id_produto = st.number_input(label='Insira o ID do produto que deseja excluir:', format='%d', step=1)

        button_submit = st.form_submit_button('Deletar')
        
        if button_submit:
            try:
                produto.deletar_produto_db(input_id_produto)
                st.success('Produto deletado com sucesso')
            except ForeignKeyViolation:
                st.error('Produto possui vendas cadastradas, exclua suas vendas antes de deletá-lo')
                db.con.rollback()

def deletar_supermercado():
    st.title('Deletar supermercado')
    
    with st.form(key='delete_supermercado'):
        input_cnpj = st.number_input(label='Insira o CNPJ que deseja excluir:', format='%d', step=1)

        button_submit = st.form_submit_button('Deletar')
        
        if button_submit:
            try:
                supermercado.deletar_supermercado_db(input_cnpj)
                st.success('Supermercado deletado com sucesso')
            except ForeignKeyViolation:
                st.error('Supermercado possui vendas cadastradas, exclua suas vendas antes de deletá-lo')
                db.con.rollback()

def deletar_venda(): 
    st.title('Deletar venda')
    
    with st.form(key='delete_venda'):
        input_id_venda = st.number_input(label='Insira o ID da venda que deseja excluir:', format='%d', step=1)

        button_submit = st.form_submit_button('Deletar')
        
        if button_submit:
            venda.deletar_venda_db(input_id_venda)
            st.success('Venda deletada com sucesso')
