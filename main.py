import streamlit as st

import page.insert as insert
import page.select as select
import page.update as update
import page.delete as delete

#criando a barra lateral do menu
st.sidebar.title('Menu')

selectbox = st.sidebar.selectbox('Clientes', ['Inserir cliente', 'Consultar clientes', 'Atualizar cliente', 'Deletar cliente'])
selectbox = st.sidebar.selectbox('Produtos', ['Inserir produto', 'Consultar produtos', 'Atualizar produto', 'Deletar produto'])
selectbox = st.sidebar.selectbox('Supermercados', ['Inserir supermercado', 'Consultar supermercados', 'Atualizar supermercado', 'Deletar supermercado'])
selectbox = st.sidebar.selectbox('Vendas', ["Inserir venda", 'Consultar vendas', 'Atualizar venda', 'Deletar venda'])

# INSERIR

if selectbox == 'Inserir cliente':
    insert.inserir_cliente()

if selectbox == 'Inserir produto':
    insert.inserir_produto()

if selectbox == 'Inserir supermercado':
    insert.inserir_supermercado()

if selectbox == 'Inserir venda':
    insert.inserir_venda()

# CONSULTAR

if selectbox == 'Consultar clientes':
    select.consultar_clientes()

if selectbox == 'Consultar produtos':
    select.consultar_produtos()

if selectbox == 'Consultar supermercados':
    select.consultar_supermercados()

if selectbox == 'Consultar vendas':
    select.consultar_vendas()

# ATUALIZAR

if selectbox == 'Atualizar cliente':
    update.atualizar_cliente()

if selectbox == 'Atualizar produto':
    update.atualizar_produto()

if selectbox == 'Atualizar supermercado':
    update.atualizar_supermercado()

if selectbox == 'Atualizar venda':
    update.atualizar_venda()

# DELETAR

if selectbox == 'Deletar cliente':
    delete.deletar_cliente()

if selectbox == 'Deletar produto':
    delete.deletar_produto()

if selectbox == 'Deletar supermercado':
    delete.deletar_supermercado()

if selectbox == 'Deletar venda':
    delete.deletar_venda()


    
