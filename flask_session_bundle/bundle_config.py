try:
    from flask_sqlalchemy_bundle import db
except ImportError:
    db = None


class BaseConfig:
    SESSION_TYPE = 'sqlalchemy' if db is not None else 'null'
    SESSION_SQLALCHEMY = db
    SESSION_SQLALCHEMY_TABLE = 'flask_sessions'


class DevConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    pass


class StagingConfig(ProdConfig):
    pass


class TestConfig(BaseConfig):
    pass
