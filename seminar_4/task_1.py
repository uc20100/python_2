# 1. Напишите функцию для транспонирования матрицы

def print_matrix(matrix):
    """
    Функция выводит матрицу на консоль
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]: >2}', end=' ')
        print()


def matrix_transpose(original_matrix: list) -> list:
    """
    Функция транспонирует матрицу

    :param original_matrix: исходная матрица
    :return: транспонированная матрица
    """
    return_result = [[0] * len(original_matrix) for i in range(len(original_matrix[0]))]

    for i in range(len(user_matrix)):
        for j in range(len(user_matrix[i])):
            return_result[j][i] = original_matrix[i][j]
    return return_result


user_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print('Исходная матрица')
print_matrix(user_matrix)

new_matrix = matrix_transpose(user_matrix)
print('\nТранспонированная матрица')
print_matrix(new_matrix)
print()
