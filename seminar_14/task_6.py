# Задание №6
# 📌 На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# 📌 Напишите 3-7 тестов pytest для данного проекта.
# 📌 Используйте фикстуры.

from user import User
from us_exception import AccessException, LevelException
import pytest


@pytest.fixture
def json_data(tmp_path):
    """
    Фикстура создания файла JSON.
    """
    f_name = tmp_path / 'user.json'
    text_json = """{"7": {"uc": "Evgeny", "vl": "Valentina", "vc": "Victor"}, "1": {"ucc": "Evgeny", "us": "user"}}"""
    with open(f_name, 'w') as f:
        f.write(text_json)
    return str(f_name)


@pytest.fixture
def user(json_data):
    """
    Фикстура объекта User c загруженными данными.

    :param json_data: фикстура создания файла JSON.
    """
    u = User()
    u.load(json_data)
    return u


def test_access_exception(user):
    """
    Тестирование ошибки AccessException.

    :param user: объект класса User.
    """
    with pytest.raises(AccessException) as e:
        user.login_system('Evgeny', 'u')
    assert str(e.value) == "Пользователя с именем 'Evgeny' и идентификатором 'u' нет в множестве"


def test_level_exception(user):
    """
    Тестирование ошибки LevelException, когда при добавлении нового пользователя его уровень меньше вашего.

    :param user: объект класса User.
    """
    with pytest.raises(LevelException) as e:
        user.login_system('Evgeny', 'uc')
        user.add_user('Jon', 'jn', 2)
    assert str(e.value) == "Уровень доступа пользователя '2' меньше вашего уровня '7', а должен быть больше или равен"


def test_non_login_user(user):
    """
    Тестирование ошибки LevelException, когда пользователь не залогинился.

    :param user: объект класса User.
    """
    with pytest.raises(LevelException) as e:
        user.add_user('Jon', 'jn', 2)
    assert str(e.value) == "Вы не залогинились."


def test_add_user(user):
    """
    Тест на добавление нового юзера в множество.

    :param user: объект класса User.
    """
    user.login_system('user', 'us')
    user.add_user('Jon', 'jn', 5)
    assert user.login_system('Jon', 'jn') == 5
