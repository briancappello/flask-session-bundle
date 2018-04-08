try:
    from flask_sqlalchemy_bundle import db
except ImportError:
    db = None


class Config:
    SESSION_TYPE = 'null' if db is None else 'sqlalchemy'
    SESSION_KEY_PREFIX = 'session:'
    SESSION_USE_SIGNER = False
    SESSION_PERMANENT = True
    SESSION_SQLALCHEMY = db
    SESSION_SQLALCHEMY_TABLE = 'flask_sessions'
    SESSION_SQLALCHEMY_MODEL = None
