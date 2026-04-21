from config.runtime import ACTUAL_STATUS
import requests
from config.config import BASE_URL, HEADERS, INVALID_ID
from config.endpoints import GET_POST_BY_ID

def test_tc_09_get_post_invalid():
    url = BASE_URL + GET_POST_BY_ID.format(id=INVALID_ID)

    response = requests.get(url, headers=HEADERS)
    ACTUAL_STATUS["test_tc_09_get_post_invalid"] = response.status_code

    assert response.status_code == 404
