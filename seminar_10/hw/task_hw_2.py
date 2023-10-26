# На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
# Первый список ваш лотерейный билет.
# Второй список содержит список чисел, которые выпали в лотерею.
# Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.
#
# Напишите класс LotteryGame, который будет иметь метод compare_lists, который будет сравнивать числа из
# вашего билета из list1 со списком выпавших чисел list2
#
# Если совпадающих чисел нет, то выведите на экран:
# Совпадающих чисел нет.
#
# Пример входных данных:

class LotteryGame:

    def __init__(self, list_1, list_2):
        self.list1 = list_1
        self.list2 = list_2

    def compare_lists(self):
        _matching_numbers = []

        for item in self.list1:
            if item in self.list2:
                _matching_numbers.append(item)
        if len(_matching_numbers) > 0:
            print(
                f'Совпадающие числа: {_matching_numbers}\nКоличество совпадающих чисел: {len(_matching_numbers)}')
        else:
            print('Совпадающих чисел нет.')
        return _matching_numbers


if __name__ == '__main__':
    list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
    list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

    game = LotteryGame(list1, list2)
    matching_numbers = game.compare_lists()
    print(matching_numbers)

