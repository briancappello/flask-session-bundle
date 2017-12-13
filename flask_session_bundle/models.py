try:
    from flask_sqlalchemy_bundle import db
    from sqlalchemy import types

    class Session(db.Model):
        __tablename__ = 'flask_sessions'

        id = db.Column(db.Integer, primary_key=True)
        session_id = db.Column(db.String(255), unique=True)
        data = db.Column(db.LargeBinary)
        expiry = db.Column(types.DateTime, nullable=True)

        def __init__(self, session_id, data, expiry):
            self.session_id = session_id
            self.data = data
            self.expiry = expiry

        def __repr__(self):
            return '<Session data %s>' % self.data

except ImportError:
    Session = None
