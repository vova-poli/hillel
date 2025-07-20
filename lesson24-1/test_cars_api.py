import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler('test_search.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


@pytest.fixture(scope="class")
def authenticated_session():
    session = requests.Session()
    url = "http://127.0.0.1:8080/auth"
    username = "test_user"
    password = "test_pass"

    logger.info("Виконую аутентифікацію користувача...")
    response = session.post(url, auth=HTTPBasicAuth(username, password))

    assert response.status_code == 200, "Аутентифікація не вдалася"
    token = response.json().get("access_token")
    assert token, "Токен не отримано"
    session.headers.update({'Authorization': f'Bearer {token}'})
    logger.info("Токен успішно отримано")

    return session


@pytest.mark.parametrize("sort_by, limit", [
    ("price", 5),
    ("year", 3),
    ("engine_volume", 7),
    ("brand", 10),
    ("price", None),
    (None, 8),
])
def test_get_cars(authenticated_session, sort_by, limit):
    url = "http://127.0.0.1:8080/cars"
    params = {}

    if sort_by:
        params["sort_by"] = sort_by
    if limit:
        params["limit"] = str(limit)

    logger.info(f"Виконую запит: GET /cars?{params}")
    response = authenticated_session.get(url, params=params)

    assert response.status_code == 200, f"Невдалий запит: {response.status_code}"
    cars = response.json()
    logger.info(f"Отримано {len(cars)} автомобілів")

    if limit:
        assert len(cars) <= int(limit), "Отримано більше результатів, ніж потрібно"

    if sort_by:
        sorted_copy = sorted(cars, key=lambda x: x[sort_by])
        assert cars == sorted_copy, f"Сортування по '{sort_by}' не відповідає очікуваному"
