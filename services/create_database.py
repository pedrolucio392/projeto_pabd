from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Numeric, MetaData
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from sqlalchemy import *

# Cria uma instância do SQLAlchemy Engine
engine = create_engine('postgresql://postgres:pabd@localhost/Supermercado_BD_mat')
metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()


# Cria uma instância da classe base declarativa
Base = declarative_base()

# Define a classe Supermercado
class Supermercado(Base):
    __tablename__ = 'supermercados'

    CNPJ = Column(Integer, primary_key=True)
    NOME_SUPERMERCADO = Column(String(30), nullable=False)
    PROPRIETARIO = Column(String(50), nullable=False)

    def __repr__(self):
        return f'Suermercado(self.CNPJ)'

# Define a classe Produto
class Produto(Base):
    __tablename__ = 'produtos'
    ID_PRODUTO = Column(Integer, primary_key=True)
    VALOR = Column(Numeric(precision=10, scale=2, asdecimal=True), nullable=False)
    NOME = Column(String(35), nullable=False)
    CATEGORIA = Column(String(35), nullable=False)

    def __repr__(self):
        return f'Profuto(self.ID_PRODUTO)'

# Define a classe Cliente
class Cliente(Base):
    __tablename__ = 'clientes'
    CPF = Column(Integer, primary_key=True)
    TELEFONE = Column(Integer, nullable=False)
    ENDERECO = Column(String(100), nullable=False)

    def __repr__(self):
        return f'Cliente(self.CPF)'

# Define a classe Venda
class Venda(Base):
    __tablename__ = 'vendas'

    ID_VENDA = Column(Integer, primary_key=True)
    DATA_VENDA = Column(Date, nullable=False)
    ID_PRODUTO = Column(Integer, ForeignKey('produtos.ID_PRODUTO'))
    CNPJ = Column(Integer, ForeignKey('supermercados.CNPJ'))
    CPF_CLIENTE = Column(Integer, ForeignKey('clientes.CPF'))

    produto = relationship("Produto")
    supermercado = relationship("Supermercado")
    cliente = relationship("Cliente")


    def __repr__(self):
        return f'Venda(self.ID_VENDA)'

# Cria todas as tabelas no banco de dados


if __name__ == '__main__':

    metadata.reflect(bind=engine)

    for table in reversed(metadata.sorted_tables):
        table.drop(engine)

    # Cria as tabelas no banco de dados

    Base.metadata.create_all(engine)