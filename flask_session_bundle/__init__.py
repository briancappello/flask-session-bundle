from flask_application_factory import Bundle


class FlaskSessionBundle(Bundle):
    module_name = __name__
    extensions_module_name = 'extension'
