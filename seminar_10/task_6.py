# Задание №6
# 📌 Доработайте задачу 5.
# 📌 Вынесите общие свойства и методы классов в класс
# Животное.
# 📌 Остальные классы наследуйте от него.
# 📌 Убедитесь, что в созданные ранее классы внесены правки.


class Animal:

    def __init__(self):
        self.planet = 'Earth'

    def view_planet(self):
        print(f'{self.planet = }')


class Birds(Animal):
    def __init__(self):
        self.habitat_birds = 'air'
        super().__init__()

    def view_habitat_birds(self):
        print(f'{self.habitat_birds = }')


class Fish(Animal):
    def __init__(self):
        self.habitat_fish = 'water'
        super().__init__()

    def view_habitat_fish(self):
        print(f'{self.habitat_fish = }')

    def view_planet(self):
        print(f'{self.planet = }')


class Cat(Animal):
    def __init__(self):
        self.habitat_cat = 'ground'
        super().__init__()

    def view_habitat_human(self):
        print(f'{self.habitat_cat = }')


if __name__ == '__main__':
    birds = Birds()
    fish = Fish()
    cat = Cat()

    birds.view_planet()
    birds.view_habitat_birds()
    fish.view_planet()
    fish.view_habitat_fish()
    cat.view_planet()
    cat.view_habitat_human()
