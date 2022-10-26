import os

from sqlmodel import create_engine, SQLModel, Session

# DATABASE_URL = os.environ.get("")
DATABASE_URL = "postgresql://ilzzjttl:6FTOl3qje7HvLgG7pbgyayreJawjcMqQ@lucky.db.elephantsql.com/ilzzjttl"
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()
