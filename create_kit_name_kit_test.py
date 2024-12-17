import sender_stand_request
import data

# Funciones de utilidad
def get_create_user_body():
    return data.user_body.copy()
def get_create_kit_body(kit_name):
    body_copy = data.kit_body.copy()
    body_copy["name"] = kit_name
    return body_copy
def get_create_kit_headers(authorization_token):
    body_copy = data.headers_for_kit_creation_for_user.copy()
    body_copy["Authorization"] = "Bearer " + authorization_token
    return body_copy
def extract_user_token_from_response(response):
    json = response.json()
    return json["authToken"]
def post_new_user_and_extract_its_token():
    # # obtenemos el body para crear un usuario
    user_body = get_create_user_body()
    # # obtener respuesta de creacion de usuario
    res = sender_stand_request.post_new_user(user_body)
    # #extraer y retornar el token que necesitamos para la creacion del kit asociado a un usuario (el duenio del token)

    return extract_user_token_from_response(res)

# Funcion para pruebas positivas
def positive_assert(kit_name):
    # El token recibido del usuario creado se guarda en la variable token
    token = post_new_user_and_extract_its_token()
    # Los headers con los datos necesarios actualizados para crear un kit para un usuario se guarda en la variable kit_headers
    kit_headers = get_create_kit_headers(token)
    # El body actualizado para crear un kit para un usuario se guarda en la variable kit_body
    kit_body = get_create_kit_body(kit_name)

    # El resultado de la solicitud para crear un nuevo kit para un/a usuario/a se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_kit_for_user(kit_headers, kit_body)

    # Comprueba si el codigo de la respuesta es 201
    assert kit_response.status_code == 201
    # Comprueba si el campo "name" de la respuesta coincide con el campo "name" del cuerpo de la solicitud
    assert kit_response.json()["name"] == kit_body["name"]

# Funcion para pruebas negativas
def negative_assert(kit_name):
    kit_body = get_create_kit_body(kit_name)
    # El token recibido del usuario creado se guarda en la variable token
    token = post_new_user_and_extract_its_token()
    # Los headers con los datos necesarios actualizados para crear un kit para un usuario se guarda en la variable kit_headers
    kit_headers = get_create_kit_headers(token)
    # El body actualizado para crear un kit para un usuario se guarda en la variable kit_body
    kit_body = get_create_kit_body(kit_name)

    # El resultado de la solicitud para crear un nuevo kit para un/a usuario/a se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_kit_for_user(kit_headers, kit_body)

    # Comprueba si el codigo de la respuesta es 400
    assert kit_response.status_code == 400

def negative_assert_no_parameter(param_name):
    # El token recibido del usuario creado se guarda en la variable token
    token = post_new_user_and_extract_its_token()
    # Los headers con los datos necesarios actualizados para crear un kit para un usuario se guarda en la variable kit_headers
    kit_headers = get_create_kit_headers(token)

    # El body actualizado para crear un kit para un usuario se guarda en la variable kit_body
    kit_body = get_create_kit_body("place_holder_value")
    # El parametro param_name se elimina de la solicitud
    kit_body.pop(param_name)

    # Guarda el resultado de llamar a la función a la variable "response"
    response = sender_stand_request.post_new_kit_for_user(kit_headers, kit_body)

    # Comprueba si la respuesta contiene el código 400
    assert response.status_code == 400

# TESTS
# Prueba 1. Creación de un nuevo kit dentro de un usuario/a
# El parámetro "name" contiene 1 caracter
def test_1_create_kit_for_user_1_letter_in_name_get_success_response():
    positive_assert("a")

# Prueba 2. Creación de un nuevo kit dentro de un usuario/a
# El parámetro "name" contiene 511 caracteres
def test_2_create_kit_for_user_511_letters_in_name_get_success_response():
    positive_assert(data.VALID_STRING_WITH_511_LETTERS)

# Prueba 3. Creación de un nuevo kit dentro de un usuario/a
# El parámetro "name" contiene 0 caracteres
def test_3_create_kit_for_user_0_letters_in_name_get_error_response():
    negative_assert("")

# Prueba 4. Creación de un nuevo kit dentro de un usuario/a
# El parámetro "name" contiene 512 caracteres
def test_4_create_kit_for_user_512_letters_in_name_get_error_response():
    negative_assert(data.VALID_STRING_WITH_512_LETTERS)

# Prueba 5. Creación de un nuevo kit dentro de un usuario/a
# El parámetro "name" contiene caracteres especiales ("№%@",")
def test_5_create_kit_for_user_special_characters_in_name_get_success_response():
    positive_assert('"№%@","')

# Prueba 6. Creación de un nuevo kit dentro de un usuario/a
# El parámetro "name" contiene espacios
def test_6_create_kit_for_user_contains_blank_characters_in_name_get_success_response():
    positive_assert(" A Aaa ")

# Prueba 7. Creación de un nuevo kit dentro de un usuario/a
# El parámetro "name" contiene numeros
def test_7_create_kit_for_user_contains_numbers_in_name_get_success_response():
    positive_assert("123")

# Prueba 8. Creación de un nuevo kit dentro de un usuario/a
# El parámetro "name" no se pasa en la solicitud
def test_8_create_kit_for_user_without_parameter_name_get_error_response():
    negative_assert_no_parameter("name")