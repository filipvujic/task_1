from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database
from config import reinit_db

class Base(DeclarativeBase):
    pass

class DbUtil():

    conn_string = 'postgresql://postgres:postgres@localhost:5432/task_1_db'
    engine = create_engine(conn_string, echo=True, isolation_level='AUTOCOMMIT')


    @classmethod
    def get_session(self):
        
        Base.metadata.create_all(bind=DbUtil.engine)
        Session = sessionmaker(bind=DbUtil.engine)
        session = Session()
        return session

    ### Initialize db and return session.
    @classmethod
    def initialize_db(self):

        ### Create database if it does not exist.
        if not database_exists(DbUtil.engine.url):
            create_database(DbUtil.engine.url)
            DbUtil.fill_data(engine=DbUtil.engine)
        else:
            ### Drop and create database if exists.
            if reinit_db:
                drop_database(DbUtil.engine.url)
                create_database(DbUtil.engine.url)
                DbUtil.fill_data(engine=DbUtil.engine)
            conn = DbUtil.engine.connect()

        return None
    

    @classmethod    
    def fill_data(self, engine: create_engine):
        from models.models import User, Pet

        session = self.get_session()

        user1 = User("Filip", "Vujic", None, "filip.vujic@qcerris.com")
        user2 = User("Nikola", "Ilic", None, "nikola.ilic@qcerris.com")
        user3 = User("Teodora", "Markovic", None, "teodora.markovic@qcerris.com")
        user4 = User("Bura", "Buric", None, "bura.buric@qcerris.com")
        user5 = User("Luka", "Vuksanovic", None, "luka.vuksanovic@qcerris.com")

        pet1 = Pet("Cat", "Mimi", 5, user1.user_profile)
        pet2 = Pet("Parrot", "Peki", 1, user2.user_profile)
        pet3 = Pet("Snake", "Sneki", 2, user3.user_profile)
        pet4 = Pet("Lizard", "Lizi", 3, user4.user_profile)
        pet5 = Pet("Koala", "Koki", 6, user5.user_profile)
        pet6 = Pet("Tiger", "Taki", 5, user2.user_profile)
        pet7 = Pet("Lion", "Laki", 1, user3.user_profile)
        pet8 = Pet("Ant", "Anta", 2, user3.user_profile)
        pet9 = Pet("Puma", "Puki", 3, user4.user_profile)
        pet10 = Pet("Skakavac", "Skaki", 6, user5.user_profile)

        ### Add users.
        session.add_all([user1, user2, user3, user4, user5])
        ### Add pets.
        session.add_all([pet1, pet2, pet3, pet4, pet5, pet6, pet7, pet8, pet9, pet10])

        session.commit()

        return None

