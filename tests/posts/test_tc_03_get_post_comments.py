from config.runtime import ACTUAL_STATUS
import requests
from config.config import BASE_URL, HEADERS, VALID_ID
from config.endpoints import GET_POST_COMMENTS

def test_tc_03_get_post_comments():
    url = BASE_URL + GET_POST_COMMENTS.format(id=VALID_ID)
    response = requests.get(url, headers=HEADERS)
    ACTUAL_STATUS["test_tc_03_get_post_comments"] = response.status_code

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    expected_keys = {"postId", "id", "name", "email", "body"}

    for item in data:
        assert expected_keys.issubset(item.keys())
        assert item["postId"] == VALID_ID
