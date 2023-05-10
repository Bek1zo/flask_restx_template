"""App."""
from .app import get_app

from flask_restx import Api

from .api.data import api as ns_data
from .api.users import api as ns_users
from .tools.common import BlueprintContainer

from .web.views import page


api = Api(
    title='Моя программа',
    version='1.0',
    description='Описание',
    doc='/apidocs/',
    validate=True
    # All API metadatas
)

api.add_namespace(ns_data, path='/data')
api.add_namespace(ns_users, path='/users')

blueprints = []
blueprints.append(BlueprintContainer(page, '/'))
