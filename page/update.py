import streamlit as st
import services.database as db

import controller.cliente as cliente
import controller.produto as produto
import controller.supermercado as supermercado
import controller.venda as venda

from psycopg2.errors import UniqueViolation, ForeignKeyViolation

# JOÃO E JEAN

def atualizar_cliente(): #FINALIZADO

    st.title('Atualizar dados do cliente')

    with st.form(key='atualizar_cliente'):
        input_cpf = st.number_input(label='Insira o seu cpf:', format='%d', step=1)
        input_novo_nome = st.text_input(label='Insira o novo nome:')
        input_novo_endereco = st.text_input(label='Insira o seu novo endereço')
        input_novo_telefone = st.number_input(label='Insira o seu novo telefone:', format='%d', step=1)

        buttom_submit = st.form_submit_button('Enviar')
        if buttom_submit:
            try:
                cliente.atualizar_cliente_db(input_cpf, input_novo_nome, input_novo_endereco, input_novo_telefone)
                st.success('Dados do cliente atualizados com sucesso')
            except ForeignKeyViolation:
                st.error('Algum dado inserido está incorreto. Verifique se os dados estão corretos.')
                db.con.rollback()

def atualizar_supermercado(): #FINALIZADO
    st.title('Atualizar dados do supermercado')

    with st.form(key='atualizar_supermercado'):
        input_cnpj = st.number_input(label='Insira o seu cnpj:', format='%d', step=1)
        input_novo_nome_supermercado = st.text_input(label='Insira o novo nome do supermercado:')
        input_novo_proprietario = st.text_input(label='Insira o novo nome do proprietário: ')

        buttom_submit = st.form_submit_button('Atualizar')
        if buttom_submit:
            try:
                supermercado.atualizar_supermercado_db(input_cnpj, input_novo_nome_supermercado, input_novo_proprietario)
                st.success('Dados do supermercado atualizados com sucesso')
            except ForeignKeyViolation:
                st.error('Algum dado inserido está incorreto. Verifique se os dados estão corretos.')
                db.con.rollback()

def atualizar_produto(): #FINALIZADO
    st.title('Atualizar dados do produto')

    with st.form(key='insert'):
        input_id_produto = st.number_input(label='Insira o ID do produto:', format='%d', step=1)
        input_novo_valor = st.number_input(label='Insira o novo valor do produto:', format='%d', step=1)
        input_novo_nome_produto = st.text_input(label='Insira o novo nome do produto:')
        input_novo_categoria = st.text_input(label='Insira o novo nome da categoria: ')

        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            try:
                produto.atualizar_produto_db(input_id_produto, input_novo_valor, input_novo_nome_produto, input_novo_categoria)
                st.success('Dados do produto atualizados com sucesso')
            except ForeignKeyViolation:
                st.error('Algum dado inserido está incorreto. Verifique se os dados estão corretos.')
                db.con.rollback()

def atualizar_venda(): #FINALIZADO
    st.title('Atualizar dados da venda')

    with st.form(key='atualizar_venda'):
        input_id_venda = st.number_input(label='Insira o ID da venda:', format='%d', step=1)
        input_nova_data_venda = st.date_input(label='Insira a nova data da venda:')
        input_novo_id_produto = st.number_input(label='Insira o novo ID do produto:', format='%d', step=1)
        input_novo_cnpj = st.number_input(label='Insira o novo CNPJ do supermercado', format='%d', step=1)
        input_novo_cpf_cliente = st.number_input(label='Insira o novo CPF do cliente:', format='%d', step=1)

        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            try:
                nova_data_venda = input_nova_data_venda.strftime('%Y-%m-%d')
                venda.atualizar_venda_db(input_id_venda, nova_data_venda, input_novo_id_produto, input_novo_cnpj, input_novo_cpf_cliente)
                st.success('Dados da venda atualizados com sucesso')
            except ForeignKeyViolation:
                st.error('Algum dado inserido está incorreto. Verifique se os dados estão corretos.')
                db.con.rollback()