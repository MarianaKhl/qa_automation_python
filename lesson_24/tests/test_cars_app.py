import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging


logging.basicConfig(level=logging.INFO, filename='test_search.log', filemode='w', format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

BASE_URL = "http://127.0.0.1:8080"


# authentication fixture that receives a token and sets it to a session
@pytest.fixture(scope='class')  # scope='class' allows you to use this session for all tests in the same class
def auth_session():
    session = requests.Session()
    # establishing a session and obtaining an access_token via the /auth endpoint
    auth_response = session.post(f"{BASE_URL}/auth", auth=HTTPBasicAuth('test_user', 'test_pass'))
    if auth_response.status_code == 200:
        access_token = auth_response.json().get("access_token")
        session.headers.update({'Authorization': f'Bearer {access_token}'})
        logger.info("Authentication was successful.")
    else:
        logger.error("Authentication failed.")
    return session


# sort_by and limit, making it easy to test the API for different combinations of query parameters
@pytest.mark.parametrize("sort_by, limit", [
    ("price", 5),
    ("year", 3),
    ("engine_volume", 7),
    ("brand", 10),
    ("price", None),
    (None, 5),
    (None, None)
])
def test_search_cars(auth_session, sort_by, limit):
    # preparation of request parameters
    params = {}
    if sort_by:
        params['sort_by'] = sort_by
    if limit:
        params['limit'] = limit

    # GET request
    response = auth_session.get(f"{BASE_URL}/cars", params=params) # GET request to the /cars endpoint

    logger.info(f"We execute the query with sort_by parameters={sort_by}, limit={limit}")
    logger.info(f"Response status code: {response.status_code}")
    logger.info(f"Respond: {response.json()}")

    assert response.status_code == 200, f"Expected status code 200, received {response.status_code}"

    # additional checks on the content of the response, for example:
    response_data = response.json()

    if limit:
        assert len(response_data) <= limit, f"Expected number of results {limit}, received {len(response_data)}"

    if sort_by:
        sorted_data = sorted(response_data, key=lambda x: x.get(sort_by))
        assert response_data == sorted_data, f"The data is not sorted by field {sort_by}"
