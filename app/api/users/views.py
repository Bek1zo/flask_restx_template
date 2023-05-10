from flask_restx import Namespace, Resource, inputs
from flask_restx.reqparse import RequestParser

from .schemas import user_out_schema, user_in_schema, msg_out_schema
from .service import get_users, create_user, delete_user, get_user, update_user

api = Namespace('Пользователи', description='CRUD пользователи')

api.models[user_out_schema.name] = user_out_schema
api.models[user_in_schema.name] = user_in_schema
api.models[msg_out_schema.name] = msg_out_schema

parser_user = RequestParser()
parser_user.add_argument('flag', type=inputs.boolean)


@api.route('/', endpoint='/')
class UserList(Resource):
    @api.expect(parser_user)
    @api.marshal_list_with(user_out_schema)
    def get(self):
        """Список пользователей"""
        args = parser_user.parse_args()
        return get_users()

    @api.expect(user_in_schema)
    @api.marshal_with(msg_out_schema)
    def post(self):
        """Создать пользователя"""
        payload = api.payload
        message = create_user(payload)
        return {'message': message}, 201


@api.route('/<id>')
@api.param('id', 'Идентификатор пользователя')
@api.response(404, 'Не найдено')
class User(Resource):
    # @api.doc('получить пользователя')
    @api.marshal_with(user_out_schema)
    def get(self, id):
        """Получить пользователя по идентификатору"""
        return get_user(id)

    @api.expect(user_in_schema)
    @api.marshal_with(msg_out_schema)
    def put(self, id):
        """Обновить пользователя"""
        payload = api.payload
        message, result = update_user(id, payload)
        if result:
            return {'message': message}, 201
        else:
            api.abort(404)

    @api.marshal_with(msg_out_schema)
    def delete(self, id):
        '''Удалить пользователя'''
        message, result = delete_user(id)
        if result:
            return {'message': message}, 201
        else:
            api.abort(404)