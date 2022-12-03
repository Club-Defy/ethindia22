from config.config import baseUrl


def register_user(user_id):
    return baseUrl + "id=" + str(user_id)