import streamlit as st

import controller.cliente as cliente

def update():
    st.title('Atualizar Cliente')
    
    with st.form(key='insert'):
        input_cpf = st.number_input(label='Insira o CPF:', format='%d', step=1)
        input_nome = st.text_input(label='Insira o nome:')
        input_endereco = st.text_input(label='Insira seu endereço')
        input_telefone = st.number_input(label='Insira seu telefone:', format='%d', step=1)

        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.atualizar_cliente(input_cpf, input_nome, input_endereco, input_telefone)
            st.success('Cliente incluido com sucesso')