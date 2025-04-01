from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Configuration do MySQLAlchemy
DATABASE_URL = "mysql+pymysql://root:55adb3@localhost:3306/todo_db"

# Criação do engine
engine = create_engine(DATABASE_URL, echo=True)
# Criação da sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Criação da base declarativa
Base = declarative_base()