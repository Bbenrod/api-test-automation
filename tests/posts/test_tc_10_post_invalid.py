from config.runtime import ACTUAL_STATUS
import requests
from config.config import BASE_URL, HEADERS, INVALID_POST
from config.endpoints import CREATE_POST

def test_tc_10_post_invalid():
    response = requests.post(
        BASE_URL + CREATE_POST,
        json=INVALID_POST,
        headers=HEADERS
    )
    ACTUAL_STATUS["test_tc_10_post_invalid"] = response.status_code

    assert response.status_code == 400
