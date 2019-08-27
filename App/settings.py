import os


def get_db_uri(dbinfo):
    db = dbinfo.get("db")
    driver = dbinfo.get("driver")
    user = dbinfo.get("user")
    password = dbinfo.get("password")
    host = dbinfo.get("host")
    port = dbinfo.get("port")
    name = dbinfo.get("name")

    return "{}+{}://{}:{}@{}:{}/{}".format(db, driver, user, password, host, port, name)


class Config:
    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.urandom(24)


class DevelopConfig(Config):
    DEBUG = True

    DATABASE = {
        "db": "mysql",
        "driver": "pymysql",
        "user": "root",
        "password": "ling1112",
        "host": "localhost",
        "port": "3306",
        "name": "test"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestingConfig(Config):
    TESTING = True

    DATABASE = {
        "db": "mysql",
        "driver": "pymysql",
        "user": "root",
        "password": "ling1112",
        "host": "localhost",
        "port": "3306",
        "name": "BJ1806FlaskProject"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):
    DATABASE = {
        "db": "mysql",
        "driver": "pymysql",
        "user": "root",
        "password": "ling1112",
        "host": "localhost",
        "port": "3306",
        "name": "test"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class StagingConfig(Config):
    DATABASE = {
        "db": "mysql",
        "driver": "pymysql",
        "user": "root",
        "password": "ling1112",
        "host": "localhost",
        "port": "3306",
        "name": "BJ1806FlaskProject"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "product": ProductConfig,
    "staging": StagingConfig,
    "default": DevelopConfig
}
