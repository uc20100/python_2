# Задание №3
# 📌 Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import unittest
from task_1 import modification_str


class TestModification(unittest.TestCase):
    def test_without_changes(self):
        self.assertEqual(modification_str('Hello World, Привет мир!'), 'Hello World, Привет мир!','Тест1 провален')

    def test_small_case(self):
        self.assertEqual(modification_str('Hello World, Привет мир!'), 'hello world, привет мир!','Тест2 провален')

    def test_no_punctuation(self):
        self.assertEqual(modification_str('Hello World, Привет мир!'), 'Hello World Привет мир','Тест3 провален')

    def test_only_latin(self):
        self.assertEqual(modification_str('Hello World, Привет мир!'), 'Hello World,  !','Тест4 провален')

    def test_all_conditions(self):
        self.assertEqual(modification_str('Hello World, Привет мир!'), 'hello world  ','Тест5 провален')


if __name__ == '__main__':
    unittest.main()
