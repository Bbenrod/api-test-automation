from config.runtime import ACTUAL_STATUS
import requests
from config.config import BASE_URL, HEADERS, VALID_POST
from config.endpoints import CREATE_POST

def test_tc_04_create_post():
    response = requests.post(
        BASE_URL + CREATE_POST,
        json=VALID_POST,
        headers=HEADERS
    )
    ACTUAL_STATUS["test_tc_04_create_post"] = response.status_code

    assert response.status_code == 201

    data = response.json()

    assert data["userId"] == VALID_POST["userId"]
    assert data["title"] == VALID_POST["title"]
    assert data["body"] == VALID_POST["body"]
    assert "id" in data
