import streamlit as st

import page.insert as insert
import page.select as select
import page.update as update
import page.delete as delete


#criando a barra lateral do menu
st.sidebar.title('Menu')

# Barra lateral inicial
opcoes_iniciais = ['Inserir', 'Consultar', 'Atualizar', 'Deletar']
selectbox_inicial = st.sidebar.selectbox('O que deseja?', opcoes_iniciais)

# INSERIR

if selectbox_inicial == 'Inserir':
    
    opcoes_inserir = ['Inserir cliente', 'Inserir produto', 'Inserir supermercado', 'Inserir venda']
    selectbox_inserir = st.sidebar.selectbox('O que desaja inserir?', opcoes_inserir)

    if selectbox_inserir == 'Inserir cliente':
        insert.inserir_cliente()

    if selectbox_inserir == 'Inserir produto':
        insert.inserir_produto()

    if selectbox_inserir == 'Inserir supermercado':
        insert.inserir_supermercado()

    if selectbox_inserir == 'Inserir venda':
        insert.inserir_venda()

# CONSULTAR

if selectbox_inicial == 'Consultar':
    
    opcoes_consultar = ['Consultar clientes', 'Consultar produtos', 'Consultar supermercados', 'Consultar vendas']
    selectbox_consultar = st.sidebar.selectbox('O que desaja consultar?', opcoes_consultar)

    if selectbox_consultar == 'Consultar clientes':
        select.consultar_clientes()

    if selectbox_consultar == 'Consultar produtos':
        select.consultar_produtos()

    if selectbox_consultar == 'Consultar supermercados':
        select.consultar_supermercados()

    if selectbox_consultar == 'Consultar vendas':
        select.consultar_vendas()

# ATUALIZAR

if selectbox_inicial == 'Atualizar':
    
    opcoes_atualizar = ['Atualizar cliente', 'Atualizar produto', 'Atualizar supermercado', 'Atualizar venda']
    selectbox_atualizar = st.sidebar.selectbox('O que desaja atualizar?', opcoes_atualizar)

    if selectbox_atualizar == 'Atualizar cliente':
        cpf_cliente = int(input('Digite seu cpf para atualizar os dados: '))
        update.atualizar_cliente(cpf_cliente)

    if selectbox_atualizar == 'Atualizar produto':
        id_produto= int(input('Digite o id do produto para atualizar os dados: '))
        update.atualizar_produto(id_produto)

    if selectbox_atualizar == 'Atualizar supermercado':
        cnpj = int(input('Digite o CNPJ para atualizar os dados: '))
        update.atualizar_supermercado(cnpj)

    if selectbox_atualizar == 'Atualizar venda':
        update.atualizar_venda()

# DELETAR

if selectbox_inicial == 'Deletar':
    
    opcoes_deletar = ['Deletar cliente', 'Deletar produto', 'Deletar supermercado', 'Deletar venda']
    selectbox_deletar = st.sidebar.selectbox('O que desaja deletar?', opcoes_deletar)

    if selectbox_deletar == 'Deletar cliente':
        delete.deletar_cliente()

    if selectbox_deletar == 'Deletar produto':
        delete.deletar_produto()

    if selectbox_deletar == 'Deletar supermercado':
        delete.deletar_supermercado()

    if selectbox_deletar == 'Deletar venda':
        delete.deletar_venda()


    
