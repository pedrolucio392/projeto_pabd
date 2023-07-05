import streamlit as st
import controller.cliente as cliente
import controller.produto as produto
import controller.supermercado as supermercado
import controller.venda as venda

# PEDRO - FINALIZADA

def consultar_clientes(): #FINALIZADA
    st.title('Consultar Clientes')
    colunas = st.columns((1, 2, 1, 2))
    campos = ['CPF', 'Nome', 'Endereço', 'Telefone']

    for coluna, campo in zip(colunas, campos):
        coluna.write(campo)

    for item in cliente.selecionar_cliente():
        col1, col2, col3, col4 = st.columns((1, 2, 1, 2))

        col1.write(item[0])
        col2.write(item[1])
        col3.write(item[2])
        col4.write(item[3])

def consultar_vendas(): #FINALIZADA
    st.title('Consultar Vendas')
    rows = venda.selecionar_venda()
    
    colunas = st.columns((1, 1, 1, 1, 1))
    campos = ['ID', 'Data', 'ID Produto', 'CNPJ', 'CPF Cliente']
    
    for coluna, campo in zip(colunas, campos):
        coluna.write(campo)
    
    for row in rows:
        col1, col2, col3, col4, col5 = st.columns((1, 1, 1, 1, 1))
        col1.write(row[0])
        col2.write(row[1])
        col3.write(row[2])
        col4.write(row[3])
        col5.write(row[4])
            
def consultar_supermercados(): #FINALIZADA
    st.title('Consultar Supermercados')
    rows = supermercado.selecionar_supermercado()
    
    colunas = st.columns((1, 1, 1))
    campos = ['CNPJ', 'Nome', 'Proprietário']
    
    for coluna, campo in zip(colunas, campos):
        coluna.write(campo)
    
    for row in rows:
        col1, col2, col3 = st.columns((1, 1, 1))
        col1.write(row[0])
        col2.write(row[1])
        col3.write(row[2])

def consultar_produtos(): #FINALIZADA
    st.title('Consultar Produtos')
    rows = produto.selecionar_produto()
    
    colunas = st.columns((1, 1, 1, 1))
    campos = ['ID', 'Valor', 'Nome', 'Categoria']
    
    for coluna, campo in zip(colunas, campos):
        coluna.write(campo)
    
    for row in rows:
        col1, col2, col3, col4 = st.columns((1, 1, 1, 1))
        col1.write(row[0])
        col2.write(row[1])
        col3.write(row[2])
        col4.write(row[3])