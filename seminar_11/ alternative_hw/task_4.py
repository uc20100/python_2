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
        self.data = [[0 for j in range(cols)] for i in range(rows)]

    def __str__(self):
        """
        Возвращает строковое представление матрицы.

        Возвращает:
        - str: строковое представление матрицы
        """
        return '\n'.join([' '.join([str(self.data[i][j]) for j in range(self.cols)]) for i in range(self.rows)])

    def __repr__(self):
        """
        Возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление матрицы
        """
        return f"Matrix({self.rows}, {self.cols})"

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - bool: True, если матрицы равны, иначе False
        """
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        """
        Определяет операцию сложения двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - Matrix: новая матрица, полученная путем сложения двух исходных матриц
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        """
        Определяет операцию умножения двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - Matrix: новая матрица, полученная путем умножения двух исходных матриц
        """
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result


