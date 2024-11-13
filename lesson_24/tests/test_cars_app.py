import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging

# Налаштування логування
# Логи зберігаються у файлі test_search.log, а також відображаються у консолі
logging.basicConfig(level=logging.INFO, filename='test_search.log', filemode='w', format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

# Базова URL-адреса сервера
BASE_URL = "http://127.0.0.1:8080"


# Фікстура для автентифікації, яка отримує токен і встановлює його для сесії
@pytest.fixture(scope='class')  # scope='class' дозволяє використовувати цю сесію для всіх тестів в одному класі.
def auth_session():
    session = requests.Session()
    # встановлення сесії та отримання access_token через ендпоінт /auth
    auth_response = session.post(f"{BASE_URL}/auth", auth=HTTPBasicAuth('test_user', 'test_pass'))
    if auth_response.status_code == 200:  # Перевірка, що статус-код відповіді дорівнює 200
        access_token = auth_response.json().get("access_token")
        session.headers.update({'Authorization': f'Bearer {access_token}'})
        logger.info("Автентифікація пройдена успішно.")
    else:
        logger.error("Не вдалося пройти автентифікацію.")
    return session


# Параметризація тестів з різними значеннями для сортування і обмеження кількості результатів
@pytest.mark.parametrize("sort_by, limit", [  # sort_by та limit, що дозволяє легко перевірити API на різні комбінації параметрів запиту.
    ("price", 5),
    ("year", 3),
    ("engine_volume", 7),
    ("brand", 10),
    ("price", None),
    (None, 5),
    (None, None)
])
def test_search_cars(auth_session, sort_by, limit):
    # Підготовка параметрів запиту
    params = {}
    if sort_by:
        params['sort_by'] = sort_by
    if limit:
        params['limit'] = limit

    # Виконання GET-запиту
    response = auth_session.get(f"{BASE_URL}/cars", params=params) # GET-запит до ендпоінту /cars.

    # Логування запиту та відповіді
    logger.info(f"Виконуємо запит з параметрами sort_by={sort_by}, limit={limit}")
    logger.info(f"Статус-код відповіді: {response.status_code}")
    logger.info(f"Відповідь: {response.json()}")

    # Перевірка статусу відповіді
    assert response.status_code == 200, f"Очікувався статус-код 200, отримано {response.status_code}"

    # Додаткові перевірки на вміст відповіді, наприклад:
    response_data = response.json()

    if limit:
        assert len(response_data) <= limit, f"Очікувана кількість результатів {limit}, отримано {len(response_data)}"

    if sort_by:
        sorted_data = sorted(response_data, key=lambda x: x.get(sort_by))
        assert response_data == sorted_data, f"Дані не відсортовані за полем {sort_by}"
