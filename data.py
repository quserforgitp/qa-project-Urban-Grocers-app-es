# Body's
# body para la creacion de un usuario para obtener un bearer token
user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}
# body para la creacion de kits para un usuario
kit_body = {
    "name": "place_holder_value"
}

# Headers
# headers necesarios para la creacion de un usuario
headers_for_user_creation = {
    "Content-Type": "application/json"
}
# headers necesarios para la creacion de un kit de usuario dentro del usuario, no dentro de una tarjeta
headers_for_kit_creation_for_user = {
    "Content-Type": "application/json",
    "Authorization": "place_holder_value"
}