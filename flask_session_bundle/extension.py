from flask_session import Session


session = Session()


EXTENSIONS = {
    'session': session,
}
