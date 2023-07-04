import psycopg2


#Fazendo a conexão com o banco de dados - Mudar de acordo com os dados do seu banco
con = psycopg2.connect(
    host='localhost',
    database='Supermercado_BD_mat',
    user='postgres',
    password='0509' 
)

#Curso da conexão
cur = con.cursor()