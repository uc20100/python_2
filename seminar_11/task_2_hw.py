# Разработайте программу для хранения и управления текстовыми и числовыми записями.
# Вам нужно создать класс Archive, который будет представлять архив и реализовывать следующую функциональность:
#
# Методы и операции:
#
# При создании экземпляра класса Archive с указанием текстовой и числовой записи (text и number), записи добавляются в
# соответствующие атрибуты archive_text и archive_number. Если архив уже существует, текущие записи (text и number)
# добавляются в архив.
#
# Метод __str__ возвращает строковое представление объекта, включая текущие записи (text и number) и архивированные
# записи (archive_text и archive_number).
#
# Метод __repr__возвращает строковое представление объекта, которое можно использовать для создания нового объекта
# того же класса с теми же записями.
#
# Архивированные записи могут быть получены через атрибуты archive_text и archive_number.
#
# Метод __new__ - это статический метод, который создает новый экземпляр класса. Первым аргументом метод __new__
# получает ссылку на класс (cls), а затем может принимать дополнительные аргументы. Метод __new__ проверяет, существует
# ли уже экземпляр класса Archive (с использованием атрибута _instance). Если экземпляр существует, то метод вместо
# создания нового экземпляра добавляет текущие значения text и number в архив (списки archive_text и archive_number)
# для уже существующего экземпляра. Если экземпляр еще не существует, метод создает новый экземпляр класса Archive с
# пустыми архивами для текстовых и числовых записей. В любом случае метод возвращает созданный или существующий
# экземпляр класса Archive.
#
# Метод __init__ - это конструктор экземпляра класса, который вызывается после создания экземпляра с использованием
# метода __new__. Метод __init__ принимает два аргумента: text (строка) и number (целое число или число с плавающей
# точкой). В методе __init__устанавливаются атрибуты text и number текущего экземпляра класса для хранения переданных
# текстовой и числовой записей. Эти записи могут быть затем добавлены в архив (списки archive_text и archive_number)
# с использованием метода __new__.

class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """
    archive_text = []
    archive_number = []
    _text = None
    _number = None

    def __new__(cls, text, number):
        instance = super().__new__(cls)
        if hasattr(cls, '_instance'):
            cls.archive_text.append(cls._text)
            cls.archive_number.append(cls._number)
        else:
            cls.archive_text = []
            cls.archive_number = []
            cls._instance = True
        cls._text = text
        cls._number = number
        return instance

    def __str__(self):
        """
         Возвращает строковое представление записей.

        :return: строковое представление записей
        """
        return f'Text is {self._text} and number is {self._number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        """
         Возвращает строковое представление записей, которое может быть использовано для создания нового объекта.

        :return: строковое представление записей, которое может быть использовано для создания нового объекта
        """
        return f"{Archive.__name__}({self.archive_text}, '{self.archive_number}')"


if __name__ == '__main__':

    archive1 = Archive("First Text", 1)
    print(archive1)
    archive2 = Archive("Second Text", 2)
    print(archive2)
    archive3 = Archive("Third Text", 3)
    print(archive1)
    print(archive3)

