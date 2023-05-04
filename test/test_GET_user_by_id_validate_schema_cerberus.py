import requests

from schemas.schema_validator_cerberus import validate_one_object_schema


def test_GET_user_by_id_validate_schema():
    response = requests.get('https://reqres.in/api/users/2')
    print(response.json())
    validate_one_object_schema(response, user_by_id_schema)


user_by_id_schema = {
    'data': {'type': 'dict', 'schema': {
        'id': {'type': 'integer'},
        'email': {'type': 'string'},
        'first_name': {'type': 'string'},
        'last_name': {'type': 'string'},
        'avatar': {'type': 'string'}}},
    'support': {'type': 'dict', 'schema':
        {'url': {'type': 'string'},
         'text': {'type': 'string'}}}
}
