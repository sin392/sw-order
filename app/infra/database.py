from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import open_alchemy

from env import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, OPENAPI_FILE

DATABASE = "mysql://{}:{}@{}/{}?charset=utf8".format(
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_NAME
)

# ref: https://openapi-sqlalchemy.readthedocs.io/en/latest/index.html#alembic
# TODO: 相対パスとか環境変数に変更したい
open_alchemy.init_yaml(spec_filename=OPENAPI_FILE)

engine = create_engine(DATABASE)

# scoped_sessionを利用するとインスタンス化時に同一のインスタンスが返される
SessionLocal = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)
