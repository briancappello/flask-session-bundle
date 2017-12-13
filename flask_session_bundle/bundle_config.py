try:
    from flask_sqlalchemy_bundle import db
    from .models import Session as SessionModel
except ImportError:
    db = None
    SessionModel = None


class BaseConfig:
    SESSION_TYPE = 'null' if db is None else 'sqlalchemy'
    SESSION_KEY_PREFIX = 'session:'
    SESSION_USE_SIGNER = False
    SESSION_PERMANENT = True
    SESSION_SQLALCHEMY = db
    SESSION_SQLALCHEMY_MODEL = SessionModel


class DevConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    pass


class StagingConfig(ProdConfig):
    pass


class TestConfig(BaseConfig):
    pass
