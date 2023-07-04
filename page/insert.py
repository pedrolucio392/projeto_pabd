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