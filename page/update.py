import streamlit as st
import controller.cliente as cliente
import controller.produto as produto
import controller.supermercado as supermercado

# JOÃO E JEAN

def atualizar_cliente(cpf_cliente): #INACABADO

    st.title('Atualizar dados do cliente')

    sql = f'UPDATE cliente SET nome = %s endereco = %s telefone = %s WHERE cpf = {cpf_cliente} '
    with st.form(key='insert'):
        input_nome = st.text_input(label='Insira o nome:')
        input_endereco = st.text_input(label='Insira seu endereço')
        input_telefone = st.number_input(label='Insira seu telefone:', format='%d', step=1)

        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.atualizar_cliente(input_nome, input_endereco, input_telefone)
            st.success('Dados do cliente atualizado com sucesso')

def atualizar_supermercado(cnpj): #INACABADA
    st.title('Atualizar dados do supermercado')

    sql = f'UPDATE cliente SET nome_supermercado = %s proprietario = %s WHERE cnpj = {cnpj}'
    with st.form(key='insert'):
        input_nome_supermercado = st.text_input(label='Insira o nome do supermercado:')
        input_proprietario = st.text_input(label='Insira o nome do proprietário: ')

        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            supermercado.atualizar_supermercado(input_nome_supermercado, input_proprietario)
            st.success('Dados do supermercado atualizado com sucesso')

def atualizar_produto(id_produto): #INACABADA
    st.title('Atualizar dados do produto')

    sql = f'UPDATE cliente SET valor = %s nome_produto = %s categoria = %s WHERE id_produto = {id_produto}'
    with st.form(key='insert'):
        input_valor = st.number_input(label='Insira o valor do produto:', format='%d', step=1)
        input_nome_produto = st.text_input(label='Insira o nome do produto:')
        input_categoria = st.text_input(label='Insira o nome da categoria: ')

        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            produto.atualizar_produto(input_valor, input_nome_produto, input_categoria)
            st.success('Dados do produto atualizado com sucesso')

def atualizar_venda(): #INACABADA
    pass