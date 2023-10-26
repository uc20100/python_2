# Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые операции с матрицами.
#
# Атрибуты класса:
#
# rows (int): Количество строк в матрице.
# cols (int): Количество столбцов в матрице.
# data (list): Двумерный список, содержащий элементы матрицы.
#
# Методы класса:
#
# __init__(self, rows, cols): Конструктор класса, который инициализирует атрибуты rows и cols, а также создает
# двумерный список data размером rows x cols и заполняет его нулями.
#
# __str__(self): Метод, возвращающий строковое представление матрицы. Возвращаемая строка представляет матрицу,
# где элементы разделены пробелами, а строки разделены символами новой строки. Например:
#
#
# 1 2 3
# 4 5 6
# __repr__(self): Метод, возвращающий строковое представление объекта, которое может быть использовано для создания
# нового объекта того же класса с такими же размерами и данными.
#
# __eq__(self, other): Метод, определяющий операцию "равно" для двух матриц. Сравнивает две матрицы и возвращает True,
# если они имеют одинаковое количество строк и столбцов, а также все элементы равны. Иначе возвращает False.
#
# __add__(self, other): Метод, определяющий операцию сложения двух матриц. Проверяет, что обе матрицы имеют одинаковые
# размеры (количество строк и столбцов). Если размеры совпадают, создает новую матрицу, где каждый элемент равен сумме
# соответствующих элементов входных матриц.
#
# __mul__(self, other): Метод, определяющий операцию умножения двух матриц. Проверяет, что количество столбцов в
# первой матрице равно количеству строк во второй матрице. Если условие выполняется, создает новую матрицу,
# где элемент на позиции [i][j] равен сумме произведений элементов соответствующей строки из первой матрицы и столбца
# из второй матрицы.

class Matrix:
    """
    Класс, представляющий матрицу.

    Атрибуты:
    - rows (int): количество строк в матрице
    - cols (int): количество столбцов в матрице
    - data (list): двумерный список, содержащий элементы матрицы

    Методы:
    - __str__(): возвращает строковое представление матрицы
    - __repr__(): возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта
    - __eq__(other): определяет операцию "равно" для двух матриц
    - __add__(other): определяет операцию сложения двух матриц
    - __mul__(other): определяет операцию умножения двух матриц
    """
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []

        for _ in range(rows):
            self.data_rows = []
            for _ in range(cols):
                self.data_rows.append(0)
            self.data.append(self.data_rows)

    def __str__(self):
        """
        Возвращает строковое представление матрицы.

        :return: строковое представление матрицы
        """
        ret_str = ''
        for i in range(self.rows):
            for j in range(self.cols):
                ret_str += f'{str(self.data[i][j])} '
            ret_str = ret_str[:-1]
            ret_str += '\n'
        return ret_str[:-1]

    def __repr__(self):
        """
        Возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта.

        :return: строковое представление матрицы
        """
        return f'{Matrix.__name__}({self.rows}, {self.cols})'

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух матриц.

        :param other: вторая матрица (Matrix)
        :return: True, если матрицы равны, иначе False
        """
        if self.cols == other.cols and self.rows == other.rows:
            for i in range(self.rows):
                for j in range(self.cols):
                    if not (self.data[i][j] == other.data[i][j]):
                        return False
            else:
                return True
        else:
            return False

    def __add__(self, other):
        """
        Определяет операцию сложения двух матриц.

        :param other: вторая матрица (Matrix)
        :return: новая матрица, полученная путем сложения двух исходных матриц
        """
        if self.cols == other.cols and self.rows == other.rows:
            _matrix = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    _matrix.data[i][j] = self.data[i][j] + other.data[i][j]
            return _matrix
        else:
            raise ValueError("Матрицы должны иметь одинаковые размеры")

    def __mul__(self, other):
        """
        Определяет операцию умножения двух матриц.

        :param other: вторая матрица (Matrix)
        :return: новая матрица, полученная путем умножения двух исходных матриц
        """
        if self.cols == other.rows:
            _matrix = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for k in range(other.cols):
                    item = 0
                    for j in range(self.cols):
                        item += self.data[i][j] * other.data[j][k]
                        _matrix.data[i][k] = item
            return _matrix
        else:
            return False


if __name__ == '__main__':
    # Создаем матрицы
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix2 = Matrix(2, 3)
    matrix2.data = [[7, 8, 9], [10, 11, 12]]

    # Выводим матрицы
    print(matrix1)

    print(matrix2)

    # Сравниваем матрицы
    print(matrix1 == matrix2)

    # Выполняем операцию сложения матриц
    matrix_sum = matrix1 + matrix2
    print(matrix_sum)

    # Выполняем операцию умножения матриц
    matrix3 = Matrix(3, 2)
    matrix3.data = [[1, 2], [3, 4], [5, 6]]

    matrix4 = Matrix(2, 2)
    matrix4.data = [[7, 8], [9, 10]]

    result = matrix3 * matrix4
    print(result)

