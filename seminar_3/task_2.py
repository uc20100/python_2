# 2. Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

example_list = [1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 8, 'fn', 'fn', 'b', 'c', 'a', 'a']
return_list = []

for item in example_list:
    if example_list.count(item) >= 2:
        if item not in return_list:
            return_list.append(item)

print(return_list)
