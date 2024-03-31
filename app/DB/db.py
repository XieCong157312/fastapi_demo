from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import DBConfig
import pymysql

pymysql.install_as_MySQLdb()


def base_generator(engine_url):
    connect_args = {}

    if "sqlite" in engine_url:
        connect_args.update({"check_same_thread": False})
        # make it possible for sqlite to allow multi-thread contact

    engine = create_engine(
        engine_url, connect_args=connect_args
    )
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    base = declarative_base()
    base.metadata.create_all(bind=engine)
    return base, session


Sqlite_Base, Sq_session = base_generator(DBConfig.get("sqlite"))
MySQL_Base, MS_session = base_generator(DBConfig.get("mysql"))


def get_db():
    db = Sq_session()
    try:
        yield db
    finally:
        db.close()

