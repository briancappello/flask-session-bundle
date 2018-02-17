from flask_unchained import Bundle

from .register_session_model_hook import RegisterSessionModelHook


class FlaskSessionBundle(Bundle):
    hooks = [RegisterSessionModelHook]
