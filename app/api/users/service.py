from .repo import get_repo_users, create_user_repo, delete_user_repo, get_repo_user, update_user_repo


def get_users():
    """

    @return:
    """
    return get_repo_users()

def get_user(id):
    """

    @return:
    """
    return get_repo_user(id)

def create_user(payload):
    """

    @param payload:
    @return:
    """
    create_user_repo(payload)
    return 'Пользователь {} успешно создан'.format(payload['name'])

def update_user(id, value):
    """

    @param id:
    @return:
    """
    q = 1
    result = update_user_repo(id, value)
    return 'Пользователь успешно обновлен', result

def delete_user(id):
    """

    @param id:
    @return:
    """
    result = delete_user_repo(id)
    return 'Пользователь успешно удален', result