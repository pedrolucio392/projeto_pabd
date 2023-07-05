import streamlit as st
import controller.cliente as cliente
import controller.produto as produto
import controller.supermercado as supermercado
import controller.venda as venda

# PEDRO - FEITO

def inserir_cliente():
    st.title('Inserir Cliente')
    
    with st.form(key='insert_cliente'):
        input_cpf = st.number_input(label='Insira o CPF:', format='%d', step=1)
        input_nome = st.text_input(label='Insira o nome:')
        input_endereco = st.text_input(label='Insira seu endereço')
        input_telefone = st.number_input(label='Insira seu telefone:', format='%d', step=1)

        button_submit = st.form_submit_button('Enviar')
        
        if button_submit:
            cliente.incluir_cliente(input_cpf, input_nome, input_endereco, input_telefone)
            st.success('Cliente incluído com sucesso')

def inserir_venda():
    st.title('Inserir dados da venda')
    
    with st.form(key='insert_venda'):
        input_data_venda = st.date_input(label='Insira a data da venda:')
        input_id_produto = st.number_input(label='Insira o ID do produto:', format='%d', step=1)
        input_cnpj = st.number_input(label='Insira o CNPJ do supermercado', format='%d', step=1)
        input_cpf_cliente = st.number_input(label='Insira o CPF do cliente:', format='%d', step=1)

        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            data_venda = input_data_venda.strftime('%Y-%m-%d')
            venda.incluir_venda(data_venda, input_id_produto, input_cnpj, input_cpf_cliente)
            st.success('Venda incluída com sucesso.')
            
def inserir_supermercado():
    st.title('Inserir dados do Supermercado')
    
    with st.form(key='insert_supermercado'):
        input_cnpj = st.number_input(label='Insira o CNPJ:', format='%d', step=1)
        input_nome_supermercado = st.text_input(label='Insira o nome do supermercado:')
        input_proprietario = st.text_input(label='Insira o nome do proprietário:')

        button_submit = st.form_submit_button('Enviar')

        if button_submit:
            supermercado.incluir_supermercado(input_cnpj, input_nome_supermercado, input_proprietario)
            st.success('Supermercado incluído com sucesso')

def inserir_produto():
    st.title('Inserir Produto')
    
    with st.form(key='insert_produto'):
        input_valor = st.number_input(label='Insira o valor:')
        input_nome = st.text_input(label='Insira o nome:')
        input_categoria = st.text_input(label='Insira a categoria:')

        button_submit = st.form_submit_button('Enviar')

        if button_submit:
            produto.incluir_produto(input_valor, input_nome, input_categoria)
            st.success('Produto incluído com sucesso')
