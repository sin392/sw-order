from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from env import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

DATABASE = "mysql://{}:{}@{}/{}?charset=utf8".format(
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_NAME
)

engine = create_engine(DATABASE)

# scoped_sessionを利用するとインスタンス化時に同一のインスタンスが返される
SessionLocal = scoped_session(
    sessionmaker(
        autocommit=True,
        autoflush=False,
        bind=engine
    )
)

# Dependency


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
