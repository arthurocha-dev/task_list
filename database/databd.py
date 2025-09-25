from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import EmailType



db = create_engine("sqlite:///database/bank.db")

EstrutureBase = declarative_base()


class User(EstrutureBase):
    __tablename__ = "users"

    idTable = Column("id", Integer, autoincrement=True, primary_key=True )
    nameTable = Column("name", String)
    emailTable = Column("email", String, unique= True )
    passwordTable = Column("password", String)
    administratorTable = Column("administrator", Boolean)


    def __init__ (self, nameP, emailP, passwordT, administratorP = False):
        self.nameTable = nameP
        self.emailTable = emailP
        self.passwordTable = passwordT
        self.administratorTable = administratorP 




class Tasks(EstrutureBase):
    __tablename__ = "tasks"

    # user_idT = Column("user_id", ForeignKey("user.id"))
    task_idT = Column("task_id", Integer, autoincrement=True, primary_key=True)
    tasks = Column("tasks", String, nullable=False)


    def __init__ (self, tasksP):
        self.tasks = tasksP


#pra CRIAR o arquivo de migração do alembic(que é quando vc altera alguma coisa na definição das classes que geram as tabelas), vc roda:
#alembic revision --autogenerate -m "mensagem qualquer"

#agora pra executar o arquivo de migração é usando alembic upgrade head




























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
