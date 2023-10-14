import sender_stand_request, data

def get_user_body(name):

    current_body = data.user_body.copy()
    current_body['firstName'] = name
    return current_body


def positive_assert(first_name):
    #El cuerpo de la solicitud actualizada se guarda en var
    user_body = get_user_body(first_name)
    #El resultado de respuesta al crear un usuario en var
    user_response = sender_stand_request.post_create_user(user_body)

    #Comprobación de resultado del post a tabla ususario
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    # El resultado de la solicitud de recepción de datos de la tabla "user_model"
    # se guarda en la variable "users_table_response"
    users_table_response = sender_stand_request.get_users_table()

    # String que debe estar en el cuerpo de respuesta
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    # Comprueba si el usuario o usuaria existe y es único/a
    assert users_table_response.text.count(str_user) == 1

def negative_assert_symbol(first_name):
    user_name = get_user_body(first_name)
    user_response = sender_stand_request.post_create_user(user_name)
    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
    assert user_response.json()["message"] == "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."

    user_table_input = sender_stand_request.get_users_table()
    str_user = user_name["firstName"]
    assert user_table_input.text.count(str_user) == 0

# Función de prueba negativa
# La respuesta contiene el siguiente mensaje de error: "No se han enviado todos los parámetros requeridos"
def negative_assert_no_firstname(user_body):
    # Guarda el resultado de llamar a la función a la variable "response"
    response = sender_stand_request.post_create_user(user_body)

    # Comprueba si la respuesta contiene el código 400
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"



# Prueba 1. Creación de un nuevo usuario o usuaria
# El parámetro "firstName" contiene dos caracteres
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Dy")

def test_create_user_15_letter_in_first_name_get_success_response():
    return positive_assert("NewFifvteenvvvn")

def test_create_user_1_letter_in_first_name_get_error_response():
    return negative_assert_symbol("X")

# Prueba 4. Error
# El parámetro "firstName" contiene 16 caracteres
def test_create_user_16_letter_in_first_name_get_error_response():
    return negative_assert_symbol("Zpoiuyuiopoiuyte")

# Prueba 5. Error
# El parámetro "firstName" contiene palabras con espacios
def test_create_user_has_space_in_first_name_get_error_response():
    return negative_assert_symbol("Name With")

# Prueba 6. Error -> no se permiten simbolos en primer nombre
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    return negative_assert_symbol("\"№%@\",")

# Prueba 7. Error
# First name no puede contener números
def test_create_user_has_number_in_first_name_get_error_response():
    return negative_assert_symbol("321")

# Prueba 8
# La solicitud no contiene el parámetro "firstName"
def test_create_user_no_first_name_get_error_response():
    return negative_assert_no_firstname("")

# Prueba 8. Error
# La solicitud no contiene el parámetro "firstName"
def test_create_user_no_first_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    user_body = data.user_body.copy()
    # El parámetro "firstName" se elimina de la solicitud
    user_body.pop("firstName")
    # Comprueba la respuesta
    return negative_assert_no_firstname(user_body)

# Prueba 9. Error
# El parámetro "firstName" contiene un string vacío
def test_create_user_empty_first_name_get_error_response():
    user_body = get_user_body("")
    negative_assert_no_firstname(user_body)

# Prueba 10. Error.
#
def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    response = sender_stand_request.post_create_user(user_body)
    assert response.status_code == 400

