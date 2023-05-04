from http import HTTPStatus

import requests
from jsonschema import validate

from schemas.user_schema import user_by_id_schema


def test_GET_user_by_id_validate_schema():
    response = requests.get('https://reqres.in/api/users/2')
    assert response.status_code == HTTPStatus.OK
    validate(instance=response.json(), schema=user_by_id_schema)
