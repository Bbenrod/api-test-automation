from config.runtime import ACTUAL_STATUS
import requests
from config.config import BASE_URL, HEADERS
from config.endpoints import GET_POSTS


def test_tc_01_get_posts():
    """
    TC-01: GET /posts
    Valida:
    - Código HTTP (200)
    - Respuesta en formato JSON (RF-1)
    - Lista de recursos
    - Estructura consistente de cada recurso (RF-2)
    """

    url = BASE_URL + GET_POSTS
    response = requests.get(url, headers=HEADERS)
    ACTUAL_STATUS["test_tc_01_get_posts"] = response.status_code

    # Validación HTTP
    assert response.status_code == 200, "Expected status code 200"

    # Validación JSON (RF-1)
    try:
        data = response.json()
    except ValueError:
        assert False, "Response is not valid JSON"

    # Validar lista
    assert isinstance(data, list), "Response should be a list of resources"
    assert len(data) > 0, "Response list should not be empty"

    # Validar estructura (RF-2)
    expected_keys = {"userId", "id", "title", "body"}

    for index, item in enumerate(data):
        assert isinstance(item, dict), f"Item at index {index} is not an object"

        assert expected_keys.issubset(item.keys()), (
            f"Item at index {index} does not contain required keys"
        )

        assert isinstance(item["userId"], int), f"userId should be int (index {index})"
        assert isinstance(item["id"], int), f"id should be int (index {index})"
        assert isinstance(item["title"], str), f"title should be string (index {index})"
        assert isinstance(item["body"], str), f"body should be string (index {index})"