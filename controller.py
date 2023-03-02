from model import Pessoas
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib


def retorna_session():
    CONN = 'sqlite:///bancofuncionario.db'
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()


class ControllerCadastro():

    @classmethod
    def verificar_dados(cls, nome, email, senha, senha2):
        if len(nome) > 50 or len(nome) < 3:
            return 2
        elif len(email) > 100:
            return 3
        elif len(senha) > 100 or len(senha) < 6:
            return 4
        elif len(senha2) > 100 or len(senha2) < 6:
            return 4

        return 1

    @classmethod
    def cadastrar(cls, nome, email, senha, senha2):
        session = retorna_session()
        usuario = session.query(Pessoas).filter(Pessoas.email == email).all()

        if len(usuario) > 0:
            return 5

        dados_cadastrados = cls.verificar_dados(nome, email, senha, senha2)

        if dados_cadastrados != 1:
            return dados_cadastrados

        if senha != senha2:
            return 7

        try:
            senha = hashlib.sha256(senha.encode()).hexdigest()
            pessoa = Pessoas(nome=nome, email=email, senha=senha)
            session.add(pessoa)
            session.commit()

        except:
            return 6


class ControllerLogin():

    @classmethod
    def login(cls, email, senha):
        session = retorna_session()
        senha = hashlib.sha256(senha.encode()).hexdigest()
        logado = session.query(Pessoas).filter(Pessoas.email == email).filter(Pessoas.senha == senha).all()

        if len(logado) == 1:
            return {'logado': True, 'id': logado[0].id}
        else:
            return False

