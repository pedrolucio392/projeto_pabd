import streamlit as st

import controller.cliente as cliente

def inserir_cliente():
    st.title('Inserir Cliente')
    
    with st.form(key='insert'):
        input_cpf = st.number_input(label='Insira o CPF:', format='%d', step=1)
        input_nome = st.text_input(label='Insira o nome:')
        input_endereco = st.text_input(label='Insira seu endereço')
        input_telefone = st.number_input(label='Insira seu telefone:', format='%d', step=1)

        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(input_cpf, input_nome, input_endereco, input_telefone)
            st.success('Cliente incluido com sucesso')

def inserir_venda():
    st.title('Inserir Venda')
    
    with st.form(key='insert'):
        input_ID_venda = st.number_input(label='Insira o ID da venda:', format='%d', step=1)
        input_data_venda = st.text_input(label='Insira a data da venda:')
        input_ID_produto = st.text_input(label='Insira id do produto:')
        input_CNPJ = st.number_input(label='Insira o cnpj da empresa:', format='%d', step=1)
        input_CPF_cliente = st.number_input(label='Insira o cpf do cliente:', format='%d', step=1)

        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(input_ID_venda, input_data_venda, input_ID_produto, input_CNPJ, input_CPF_cliente)
            st.success('Venda incluída com sucesso.')
            
def inserir_supermercado():
    st.title('Inserir Dados do Supermercado')
    
    with st.form(key='insert'):
        input_cnpj = st.number_input(label='Insira o CNPJ da empresa:', format='%d', step=1)
        input_nome_supermercado = st.text_input(label='Insira o nome do supermercado:')
        input_nome_proprietario = st.text_input(label='Insira o nome do proprietário:')

        buttom_submit = st.form_submit_button('Enviar')


    if buttom_submit:
        cliente.incluir(input_cnpj, input_nome_supermercado, input_nome_proprietario)
        st.success('Dados do Supermercado incluido com sucesso!')

def inserir_produto():
    st.title('Inserir Produto')
    
    with st.form(key='insert'):
        input_valor = st.number_input(label='Insira o valor:', format='%d', step=1)
        input_nome = st.text_input(label='Insira o nome do produto:')
        input_categoria = st.text_input(label='Insira a categoria do produto:')


        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:

            cliente.incluir(input_valor, input_nome, input_categoria)
            st.success('Produto incluido com sucesso!')
