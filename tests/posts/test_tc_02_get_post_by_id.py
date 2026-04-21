from config.runtime import ACTUAL_STATUS
import requests
from config.config import BASE_URL, HEADERS, VALID_ID
from config.endpoints import GET_POST_BY_ID


def test_tc_02_get_post_by_id():
    """
    TC-02: GET /posts/{id}
    Valida:
    - Código HTTP (200)
    - Respuesta en formato JSON
    - Objeto individual (no lista)
    - Estructura consistente (RF-2)
    - El ID retornado coincide con el solicitado (RF-3)
    """

    url = BASE_URL + GET_POST_BY_ID.format(id=VALID_ID)
    response = requests.get(url, headers=HEADERS)
    ACTUAL_STATUS["test_tc_02_get_post_by_id"] = response.status_code

    # Validación HTTP
    assert response.status_code == 200, "Expected status code 200"

    # Validación JSON
    try:
        data = response.json()
    except ValueError:
        assert False, "Response is not valid JSON"

    # Validar que sea objeto
    assert isinstance(data, dict), "Response should be a single resource object"

    # Validar estructura (RF-2)
    expected_keys = {"userId", "id", "title", "body"}
    assert expected_keys.issubset(data.keys()), "Missing required keys in response"

    # Validar tipos
    assert isinstance(data["userId"], int), "userId should be int"
    assert isinstance(data["id"], int), "id should be int"
    assert isinstance(data["title"], str), "title should be string"
    assert isinstance(data["body"], str), "body should be string"

    # Validar coherencia del ID (RF-3)
    assert data["id"] == VALID_ID, "Returned ID does not match requested ID"