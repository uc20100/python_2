# Задание №2
# 📌 Создайте функцию аналог get для словаря.
# 📌 Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# 📌 При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# 📌 Реализуйте работу через обработку исключений.


def get_dict(dict_, key, default_value):
    try:
        return dict_[key]
    except KeyError:
        return default_value


if __name__ == '__main__':
    d = dict(key1=1, key2=2, key3=3)
    print(f"{get_dict(d,'key4',None) = }")
    print(f"{get_dict(d,'key1',None) = }")
