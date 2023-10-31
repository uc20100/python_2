# Задание №3
# 📌 Создайте класс с базовым исключением и дочерние классы-
# исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class UsException(BaseException):
    pass


class LevelException(UsException):
    pass


class AccessException(UsException):
    pass
