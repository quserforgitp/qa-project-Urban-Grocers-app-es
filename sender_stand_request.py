import configuration
import requests
import data

# url para creacion de usuario
url_create_user = configuration.URL_SERVICE + configuration.CREATE_USER_PATH
# url para creacion de kits para el usuario
url_create_kit_for_specific_user = configuration.URL_SERVICE + configuration.KITS_PATH

# Funcion para crear un nuevo usuario
def post_new_user(body):
    return requests.post(
        url=url_create_user,
        headers=data.headers_for_user_creation,
        json=body
    )
# Funcion para crear un nuevo kit para un usuario
def post_new_kit_for_user(kit_headers, kit_body):
    return requests.post(
        url=url_create_kit_for_specific_user,
        headers=kit_headers,
        json=kit_body
    )