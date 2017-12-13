from flask_session import (
    Session as BaseSession,
    SqlAlchemySessionInterface as BaseSqlAlchemySessionInterface,
)

from .models import Session as SessionModel


class SqlAlchemySessionInterface(BaseSqlAlchemySessionInterface):
    def __init__(self, db, key_prefix, use_signer=False,
                 permanent=True, model_class=SessionModel):
        self.db = db
        self.key_prefix = key_prefix
        self.use_signer = use_signer
        self.permanent = permanent
        self.sql_session_model = model_class


class Session(BaseSession):
    def _get_interface(self, app):
        if app.config['SESSION_TYPE'] == 'sqlalchemy':
            return SqlAlchemySessionInterface(
                db=app.config['SESSION_SQLALCHEMY'],
                key_prefix=app.config['SESSION_KEY_PREFIX'],
                use_signer=app.config['SESSION_USE_SIGNER'],
                permanent=app.config['SESSION_PERMANENT'],
                model_class=app.config['SESSION_SQLALCHEMY_MODEL'])
        return super()._get_interface(app)


session = Session()


EXTENSIONS = {
    'session': session,
}
