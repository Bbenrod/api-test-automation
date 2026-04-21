from config.runtime import ACTUAL_STATUS
import requests
from config.config import BASE_URL, HEADERS, INVALID_ID, VALID_POST
from config.endpoints import UPDATE_POST_PUT

def test_tc_11_put_invalid():
    url = BASE_URL + UPDATE_POST_PUT.format(id=INVALID_ID)

    response = requests.put(
        url,
        json=VALID_POST,
        headers=HEADERS
    )
    ACTUAL_STATUS["test_tc_11_put_invalid"] = response.status_code

    assert response.status_code == 404
