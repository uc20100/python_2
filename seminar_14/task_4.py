# Задание №4
# 📌 Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import pytest
from task_1 import modification_str


def test_without_changes():
    assert modification_str('hello world') == 'hello world', 'Тест1 провален'


def test_small_case():
    assert modification_str('Hello World') == 'hello world', 'Тест2 провален'


def test_no_punctuation():
    assert modification_str('hello world!') == 'hello world', 'Тест3 провален'


def test_only_latin():
    assert modification_str('hello world_Привет_мир') == 'hello world', 'Тест4 провален'


def test_all_conditions():
    assert modification_str('Hello World, Привет мир!') == 'hello world  ', 'Тест5 провален'


if __name__ == '__main__':
    pytest.main()
