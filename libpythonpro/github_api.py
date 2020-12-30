import requests


def buscar_avatar(usuario):
    """
    Buscar o avatar de um usuário no github
    :param usuario: str com nome de usuário do github
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']
