import streamlit as st

import page.insert as insert
import page.select as select

#criando a barra lateral do menu
st.sidebar.title('Menu')

selectbox = st.sidebar.selectbox('Clientes', ['Inserir cliente', 'Consultar clientes'])
selectbox = st.sidebar.selectbox('Produtos', ['Inserir produto', 'Consultar produtos'])
selectbox = st.sidebar.selectbox('Supermercados', ['Inserir supermercado', 'Consultar supermercados'])
selectbox = st.sidebar.selectbox('Vendas', ["Inserir venda", 'Consultar vendas'])


if selectbox == 'Inserir cliente':
    insert.inserir_cliente()

if selectbox == 'Inserir produto':
    insert.inserir_produto()

if selectbox == 'Inserir supermercado':
    insert.inserir_supermercado()

if selectbox == 'Inserir venda':
    insert.inserir_venda()

if selectbox == 'Consultar clientes':
    select.consultar_clientes()

if selectbox == 'Consultar produtos':
    select.consultar()

if selectbox == 'Consultar supermercados':
    select.consultar()

if selectbox == 'Consultar vendas':
    select.consultar()

    
