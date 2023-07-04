import streamlit as st
import controller.cliente as cliente

# PEDRO

def consultar_clientes(): #INACABADA
    st.title('Consultar Clientes')
    colunas = st.columns((1,2,1,2))
    campos = ['CPF', 'Nome', 'Endereço', 'Telefone', 'Excluir']
    
    for coluna, campo in zip(colunas, campos):
        coluna.write(campo)
    
    for item in cliente.selecionar():
        col1, col2, col3, col4, col5 = st.columns((1,2,1,2,1))
        
        col1.write(item[0])
        col2.write(item[1])
        col3.write(item[2])
        col4.write(item[3])
        button_excluir = col5.empty()
        on_click_excluir = button_excluir.button('x', 'btnExcluir' + str(item[0]))
        
        if on_click_excluir:
            continue
            #cliente.excluir(item[0])

def consultar_vendas(): #INACABADA
    pass
            
def consultar_supermercados(): #INACABADA
    pass

def consultar_produtos(): #INACABADA
    pass