from flask_application_factory import Bundle, ModelTuple


class FlaskSessionBundle(Bundle):
    module_name = __name__
    extensions_module_name = 'extension'

    def post_configure_app(self, app, bundles: list):
        super().post_configure_app(app, bundles)
        self.app = app

    def get_models(self):
        if self.app.config.get('SESSION_TYPE') != 'sqlalchemy':
            return []
        return [ModelTuple('Session', self.app.session_interface.sql_session_model)]
