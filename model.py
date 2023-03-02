from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONN = 'sqlite:///bancofuncionario.db'

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(100))
    senha = Column(String(100))

Base.metadata.create_all(engine)
