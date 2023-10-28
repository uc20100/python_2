# Задание №3
# 📌 Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.

class Value:
    # def __init__(self, param):
    #     self.param = param

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    @staticmethod
    def validate(value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if value is not None and value < 1:
            raise ValueError(f'Значение {value} должно быть больше или равно 1')


class Generator:
    stop = Value()
    start = Value()
    step = Value()

    def __init__(self, stop: int, start: int = 1, step: int = 1):
        self.stop = stop
        self.start = start
        self.step = step
        self._count = start

    def __iter__(self):
        return self

    def __next__(self):
        while self._count <= self.stop:
            self._count += self.step
            return self._count - self.step
        raise StopIteration


if __name__ == '__main__':
    g = Generator(1)
    for i in g:
        print(i)
