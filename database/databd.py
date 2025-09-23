from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base



db = create_engine("sqlite:///database/")































# ##############################################
# # 1) SQLAlchemy Core (sqlalchemy)
# ##############################################
# from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# # Criar conexão (engine)
# engine = create_engine("sqlite:///meubanco.db")

# # Metadata = catálogo das tabelas
# metadata = MetaData()

# # Criar tabela "usuarios" no estilo SQL puro
# usuarios_table = Table(
#     "usuarios",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("nome", String),
#     Column("email", String),
# )

# metadata.create_all(engine)  # cria no banco


# ##############################################
# # 2) ORM (sqlalchemy.orm)
# ##############################################
# from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# # Base para criar classes ↔ tabelas
# Base = declarative_base()

# # Criar modelo (classe que vira tabela)
# class Usuario(Base):
#     __tablename__ = "usuarios_orm"
#     id = Column(Integer, primary_key=True)
#     nome = Column(String)
#     email = Column(String)

# # Criar tabelas no banco
# Base.metadata.create_all(engine)

# # Criar sessão para manipular objetos
# Session = sessionmaker(bind=engine)
# session = Session()

# # Inserir dados via ORM
# novo_user = Usuario(nome="Arthur", email="arthur@example.com")
# session.add(novo_user)
# session.commit()


# ##############################################
# # 3) SQLAlchemy Utils (sqlalchemy_utils)
# ##############################################
# # Biblioteca externa com tipos e funções extras
# from sqlalchemy_utils import EmailType, database_exists, create_database

# # Checar e criar banco, se não existir
# if not database_exists(engine.url):
#     create_database(engine.url)

# # Exemplo de modelo usando EmailType (campo validado como email)
# class UsuarioComEmail(Base):
#     __tablename__ = "usuarios_utils"
#     id = Column(Integer, primary_key=True)
#     email = Column(EmailType)  # já valida se é email válido!


# ##############################################
# # 4) sqlalchemy_utils.types
# ##############################################
# # Submódulo só com tipos prontos
# from sqlalchemy_utils.types import UUIDType

# import uuid

# class UsuarioComUUID(Base):
#     __tablename__ = "usuarios_uuid"
#     id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
#     nome = Column(String)
