import os
from flask import Flask

# from .web.views import page


def internal_server_error(e):
    print(e)
    return 'Ошибка сервера {}'.format(str(e)[:500] + '...'), 500

def get_app(config) -> Flask:
    """Get flask application."""

    app = Flask(__name__)
    app.config.from_object(config)

    # Register the blueprint with the Flask app
    from . import blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint.obj, url_prefix=blueprint.url_prefix)
    app.register_error_handler(Exception, internal_server_error)

    from . import api
    api.init_app(app)

    # ///// Раскомментировать для создания таблиц, не забыть закомментировать /////

    # from sqlalchemy import create_engine
    # from .models import Base
    # from .models.models import Data, User
    # Base.metadata.create_all(create_engine(app.config.get('DB_URI', '')))

    return app
