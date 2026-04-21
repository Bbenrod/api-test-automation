from config.runtime import ACTUAL_STATUS
import requests
from config.config import BASE_URL, HEADERS, VALID_ID
from config.endpoints import UPDATE_POST_PATCH

def test_tc_06_patch_post():
    payload = {"title": "Updated title"}

    url = BASE_URL + UPDATE_POST_PATCH.format(id=VALID_ID)

    response = requests.patch(
        url,
        json=payload,
        headers=HEADERS
    )
    ACTUAL_STATUS["test_tc_06_patch_post"] = response.status_code

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == payload["title"]
