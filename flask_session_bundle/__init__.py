from flask_unchained import Bundle

from .register_session_model_hook import RegisterSessionModelHook


class FlaskSessionBundle(Bundle):
    extensions_module_name = 'extension'
    hooks = [RegisterSessionModelHook]
