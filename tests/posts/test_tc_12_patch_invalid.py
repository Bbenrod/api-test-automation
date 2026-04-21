from config.runtime import ACTUAL_STATUS
import requests
from config.config import BASE_URL, HEADERS, INVALID_ID
from config.endpoints import UPDATE_POST_PATCH

def test_tc_12_patch_invalid():
    url = BASE_URL + UPDATE_POST_PATCH.format(id=INVALID_ID)

    response = requests.patch(
        url,
        json={"title": "invalid"},
        headers=HEADERS
    )
    ACTUAL_STATUS["test_tc_12_patch_invalid"] = response.status_code

    assert response.status_code == 404
