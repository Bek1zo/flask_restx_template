from . import schemas
from ...models.models import User
from ...session import session_scope


def get_repo_users():
    """

    @return:
    """
    with session_scope() as session:
        query = session.query(User)
        query = query.all()
        return schemas.UserSchema(many=True).dump(query)

def get_repo_user(id):
    """

    @return:
    """
    with session_scope() as session:
        query = session.query(User).filter(User.id == id)
        query = query.first()
        return schemas.UserSchema(many=False).dump(query)

def create_user_repo(payload):
    """

    @param payload:
    @return:
    """
    with session_scope() as session:
        user_row = User(**payload)
        session.add(user_row)


def update_user_repo(id, value):
    """

    @param id:
    @return:
    """
    with session_scope() as session:
        return  session.query(User).filter(User.id == id).update(value, synchronize_session=False)

def delete_user_repo(id):
    """

    @param id:
    @return:
    """
    with session_scope() as session:
        return session.query(User).filter(User.id == id).delete()
