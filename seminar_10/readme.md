# ДЗ по "Погружение в Python (семинары)"

## Семинар 10. ООП. Начало
* Задание №1
  - Создайте класс окружность.
  - Класс должен принимать радиус окружности при создании
экземпляра.
  - У класса должно быть два метода, возвращающие длину
окружности и её площадь.
  
* Задание №2
  - Создайте класс прямоугольник.
  - Класс должен принимать длину и ширину при создании
экземпляра.
  - У класса должно быть два метода, возвращающие периметр
и площадь.
  - Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.

* Задание №3
  - Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
  - У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
  - Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.

* Задание №4
  - Создайте класс Сотрудник.
  - Воспользуйтесь классом человека из прошлого задания.
  - У сотрудника должен быть:
    - шестизначный идентификационный номер
    - уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь

* Задание №5
  - Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
  - У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
  - Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.

* Задание №6
  - Доработайте задачу 5.
  - Вынесите общие свойства и методы классов в класс
Животное.
  - Остальные классы наследуйте от него.
  - Убедитесь, что в созданные ранее классы внесены правки.

* Домашнее задание
  - Решить задачи, которые не успели решить на семинаре.
  - Доработаем задачи 5-6. Создайте класс-фабрику.
    - Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
    - Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.
  - Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов
экземпляра.