from flask_restx import Model, fields


# note_schema = Model('Примечание', {
#     'id': fields.String(required=True, description='Идентификатор примечания'),
#     'note': fields.String(required=True, description='Текст примечания'),
# })


data_schema = Model('Data', {
    'id': fields.String(required=True, description='Идентификатор информации'),
    'name': fields.String(required=True, description='Имя информации'),
    # 'note': fields.List(fields.Nested(note_schema, required=True, description='Примечание'))
})