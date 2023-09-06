# 4. Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

def backpack_options(weight_limit: int, things_value: dict) -> list:
    """
    Предлагает варианты комплектации рюкзака, в зависимости от макс. веса
    :param weight_limit: лимит загрузки рюкзака
    :param things_value: список вещей
    :return: возможные варианты комплектации
    """
    return_list = []
    len_name = 0
    for i in things:
        len_name += len(i) + 2
    n_variant = 1
    for i in range(1, (2 ** len(things_value))):
        str_backpack = ''
        bin_status = bin(i).rjust(len(things_value) + 2, '0')
        bin_status = bin_status.replace('0b', '')
        weight = 0
        for j, item in enumerate(things_value):
            if bin_status[j] == '1':
                str_backpack += f' {item},'
                weight += things_value[item]
        if len(str_backpack) > 0:
            str_backpack = str_backpack[:-1]
        if weight <= weight_limit:
            str_backpack = f'Вариант {n_variant: <7}  ' + f'{str_backpack: <{len_name}}' + f' Вес: {weight: >5}\r'
            n_variant += 1
            return_list.append(str_backpack)
    return return_list


BACKPACK_WEIGHT = 15
things = dict(еда=5, посуда=3, одежда=5, спальный_мешок=4, палатка=10, инвентарь=7)

list_variant = backpack_options(weight_limit=BACKPACK_WEIGHT, things_value=things)
for variant in list_variant:
    print(variant)
