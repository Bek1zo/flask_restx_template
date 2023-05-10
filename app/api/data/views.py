from flask_restx import Namespace, Resource
from .schemas import data_schema
from ..users.schemas import msg_out_schema

api = Namespace('Информация', description='Информация')

api.models[data_schema.name] = data_schema

info = [
    {'id': '1', 'name': 'Senja'},
]


@api.route('/')
class DataList(Resource):
    @api.doc('список информации')
    @api.marshal_list_with(data_schema)
    def get(self):
        '''Список всей информации'''
        return info

    # @api.expect(course_input_model)
    @api.expect(data_schema)
    @api.marshal_with(msg_out_schema)
    def post(self):
        '''Добавить информацию'''
        payload = api.payload
        info.append(payload)
        return {'message': 'ok'}, 201


@api.route('/<id>')
@api.param('id', 'идентификатор информации')
@api.response(404, 'Информация не найдена')
class Cat(Resource):
    @api.doc('информация')
    @api.marshal_with(data_schema)
    def get(self, id):
        '''Запрос одной информации'''
        for i in info:
            if i['id'] == id:
                return i
        api.abort(404)





