from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Numeric, MetaData
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from sqlalchemy import *

# Cria uma instância do SQLAlchemy Engine
engine = create_engine('postgresql://postgres:0509@localhost/Supermercado_BD_mat') # Mudar de acordo com as informações do seu banco
metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()


# Cria uma instância da classe base declarativa
Base = declarative_base()

# Define a classe Supermercado
class Supermercado(Base):
    __tablename__ = 'supermercados'

    cnpj = Column(Integer, primary_key=True)
    nome_supermercado = Column(String(30), nullable=False)
    proprietario = Column(String(50), nullable=False)

    def __repr__(self):
        return f'Suermercado(self.cnpj)'

# Define a classe Produto
class Produto(Base):
    __tablename__ = 'produtos'
    id_produto = Column(Integer, primary_key=True)
    valor = Column(Numeric(precision=10, scale=2, asdecimal=True), nullable=False)
    nome = Column(String(35), nullable=False)
    categoria = Column(String(35), nullable=False)

    def __repr__(self):
        return f'Profuto(self.id_produto)'

# Define a classe Cliente
class Cliente(Base):
    __tablename__ = 'clientes'
    cpf = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(Integer, nullable=False)
    endereco = Column(String(100), nullable=False)

    def __repr__(self):
        return f'Cliente(self.cpf)'

# Define a classe Venda
class Venda(Base):
    __tablename__ = 'vendas'

    id_venda = Column(Integer, primary_key=True)
    data_venda = Column(Date, nullable=False)
    id_produto = Column(Integer, ForeignKey('produtos.id_produto'))
    cnpj = Column(Integer, ForeignKey('supermercados.cnpj'))
    cpf_cliente = Column(Integer, ForeignKey('clientes.cpf'))

    produto = relationship("Produto")
    supermercado = relationship("Supermercado")
    cliente = relationship("Cliente")


    def __repr__(self):
        return f'Venda(self.id_venda)'

# Cria todas as tabelas no banco de dados


if __name__ == '__main__':

    metadata.reflect(bind=engine)

    for table in reversed(metadata.sorted_tables):
        table.drop(engine)

    # Cria as tabelas no banco de dados

    Base.metadata.create_all(engine)