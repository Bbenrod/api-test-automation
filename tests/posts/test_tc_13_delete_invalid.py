from config.runtime import ACTUAL_STATUS
import requests
from config.config import BASE_URL, HEADERS, INVALID_ID
from config.endpoints import DELETE_POST

def test_tc_13_delete_invalid():
    url = BASE_URL + DELETE_POST.format(id=INVALID_ID)

    response = requests.delete(url, headers=HEADERS)
    ACTUAL_STATUS["test_tc_13_delete_invalid"] = response.status_code

    assert response.status_code == 404
