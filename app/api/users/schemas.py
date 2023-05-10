from flask_restx import fields, Model
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ...models.models import User


# ///// Входящие, исходящие схемы /////
user_in_schema = Model('UserIn', {
    'id': fields.String(required=False, description='Идентификатор информации'),
    'name': fields.String(required=True, description='Имя информации'),
})

user_out_schema = Model('UserOut', {
    'id': fields.String(required=True, description='Идентификатор информации'),
    'name': fields.String(required=True, description='Имя информации'),
    # 'note': fields.List(fields.Nested(note_schema, required=True, description='Примечание'))
})

msg_out_schema = Model('MsgOut', {
    'message': fields.String(required=True, description='Текст сообщения')
})

# ///// Атосхемы /////
class UserSchema(SQLAlchemyAutoSchema):
    """Автосхема пользователя"""
    class Meta:
        """Meta."""
        model = User
        include_relationships = True
        include_fk = True