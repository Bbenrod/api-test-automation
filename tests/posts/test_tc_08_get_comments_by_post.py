from config.runtime import ACTUAL_STATUS
import requests
from config.config import BASE_URL, HEADERS, VALID_ID
from config.endpoints import GET_COMMENTS_BY_POST

def test_tc_08_get_comments_by_post():
    response = requests.get(
        BASE_URL + GET_COMMENTS_BY_POST,
        params={"postId": VALID_ID},
        headers=HEADERS
    )
    ACTUAL_STATUS["test_tc_08_get_comments_by_post"] = response.status_code

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    for item in data:
        assert item["postId"] == VALID_ID
