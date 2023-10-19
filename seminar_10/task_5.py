# Задание №5
# 📌 Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# 📌 У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# 📌 Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Birds:
    def __init__(self):
        self.planet = 'Earth'
        self.habitat_birds = 'air'

    def view_habitat_birds(self):
        print(f'{self.habitat_birds = }')

    def view_planet(self):
        print(f'{self.planet = }')


class Fish:
    def __init__(self):
        self.planet = 'Earth'
        self.habitat_fish = 'water'

    def view_habitat_fish(self):
        print(f'{self.habitat_fish = }')

    def view_planet(self):
        print(f'{self.planet = }')


class Cat:
    def __init__(self):
        self.planet = 'Earth'
        self.habitat_cat = 'ground'

    def view_habitat_human(self):
        print(f'{self.habitat_cat = }')

    def view_planet(self):
        print(f'{self.planet = }')


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