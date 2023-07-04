import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('Inserir Dados')
    
    with st.form(key='insert'):
        input_cpf = st.number_input(label='Insira o CPF:', format='%d', step=1)
        input_nome = st.text_input(label='Insira o nome:')
        input_endereco = st.text_input(label='Insira seu endereço')
        input_telefone = st.number_input(label='Insira seu telefone:', format='%d', step=1)

        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(input_cpf, input_nome, input_endereco, input_telefone)
            st.success('Cliente incluido com sucesso')

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