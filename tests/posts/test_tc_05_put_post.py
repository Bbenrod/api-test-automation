from config.runtime import ACTUAL_STATUS
import requests
from config.config import BASE_URL, HEADERS, VALID_POST, VALID_ID
from config.endpoints import UPDATE_POST_PUT

def test_tc_05_put_post():
    url = BASE_URL + UPDATE_POST_PUT.format(id=VALID_ID)

    response = requests.put(
        url,
        json=VALID_POST,
        headers=HEADERS
    )
    ACTUAL_STATUS["test_tc_05_put_post"] = response.status_code

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == VALID_POST["title"]
    assert data["body"] == VALID_POST["body"]
