BASE_URL = "https://jsonplaceholder.typicode.com"

HEADERS = {
    "Content-Type": "application/json; charset=UTF-8"
}

# Datos válidos para pruebas positivas (POST / PUT / PATCH)
VALID_POST = {
    "title": "Test title",
    "body": "Test body",
    "userId": 1
}

# Datos inválidos (para TC-10)
INVALID_POST = {
    "title": "",          # vacío
    "body": None,         # nulo
    "userId": "invalid"   # tipo incorrecto
}

# IDs
VALID_ID = 1
INVALID_ID = 99999