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


class Fish:
    def __init__(self):
        self.planet = 'Earth'
        self.habitat_fish = 'water'

    def view_habitat_fish(self):
        print(f'{self.habitat_fish = }')


class Human:
    def __init__(self):
        self.planet = 'Earth'
        self.habitat_human = 'ground'

    def view_habitat_human(self):
        print(f'{self.habitat_human = }')


if __name__ == '__main__':
    birds = Birds()
    fish = Fish()
    human = Human()

    print(f'{birds.planet = }')
    birds.view_habitat_birds()
    print(f'{fish.planet = }')
    fish.view_habitat_fish()
    print(f'{human.planet = }')
    human.view_habitat_human()