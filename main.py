import streamlit as st

import page.insert as insert
import page.select as select
import page.update as update

#criando a barra lateral do menu
st.sidebar.title('Menu')
selectbox_cliente = st.sidebar.selectbox('Cliente', ['Inserir', 'Consultar', 'Atualizar'])
selectbox_produto = st.sidebar.selectbox('Produto', ['Inserir', 'Consultar', 'Atualizar'])

if selectbox_cliente == 'Inserir':
    insert.inserir()

if selectbox_cliente == 'Consultar':
    select.consultar()

if selectbox_cliente == 'Atualizar':
    update.update()


    
