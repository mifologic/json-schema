from assertpy import assert_that, soft_assertions
from cerberus import Validator

# создаём объект Validator, require_all=True - значит, все поля схемы обязательны
validator = Validator(require_all=True)


def validate_one_object_schema(response, schema):
    # проверяем, что вызов метода возвращает 200
    assert_that(response.status_code).is_equal_to(200)
    # soft_assertions позволяют проверить сразу всю схему
    with soft_assertions():
        # проверяем, что ответ соответствует схеме
        is_valid = validator.validate(response.json(), schema)
        # проверяем, что всё валидно
        assert_that(is_valid, description=validator.errors).is_true()
