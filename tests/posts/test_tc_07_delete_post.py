from config.runtime import ACTUAL_STATUS
import requests
from config.config import BASE_URL, HEADERS, VALID_ID
from config.endpoints import DELETE_POST

def test_tc_07_delete_post():
    url = BASE_URL + DELETE_POST.format(id=VALID_ID)

    response = requests.delete(url, headers=HEADERS)
    ACTUAL_STATUS["test_tc_07_delete_post"] = response.status_code

    assert response.status_code in [200, 204]
