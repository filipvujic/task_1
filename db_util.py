from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database
from config import reinit_db

class Base(DeclarativeBase):
    pass

class DbUtil:

    ### Initialize db and return session.
    @classmethod
    def initialize_db(self):

        conn_string = 'postgresql://postgres:postgres@localhost:5432/task_1_db'
        engine = create_engine(conn_string, echo=True, isolation_level='AUTOCOMMIT')


        ### Create database if it does not exist.
        if not database_exists(engine.url):
            create_database(engine.url)
        else:
            ### Drop and create database if exists.
            if reinit_db:
                drop_database(engine.url)
            create_database(engine.url)
            conn = engine.connect()

        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

