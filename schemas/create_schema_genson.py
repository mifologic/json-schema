import requests

from genson import SchemaBuilder


def create_json_schema(method):
    """
    Create new json-schema from method.
    :param method: link for schema creation
    :return: created json-schema
    """
    # вызываем метод и получаем ответ
    response = requests.get(method)
    # создаём объект SchemaBuilder и сохраняем в переменную
    builder = SchemaBuilder()
    # вызываем у SchemaBuilder метод add_object и на вход передаём ответ метода в json
    builder.add_object(response.json())
    # возвращаем ответ в виде автоматически сгенерированной json-схемы
    return builder.to_schema()


# печатаем схему
print(create_json_schema('https://reqres.in/api/users/2'))
