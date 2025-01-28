# 9 практическая, 3 вариант, задание 2
def find_max_element_and_its_position(matrix):
    """
    Находит наибольший элемент в матрице и его координаты.

    Args:
        matrix: Двумерный список (список списков), представляющий матрицу.

    Returns:
        Кортеж (max_val, max_row, max_col): Наибольший элемент, его строка и столбец.
    """
    if not matrix:
        return None, None, None  # Возвращаем None, если матрица пуста

    max_val = matrix[0][0]
    max_row = 0
    max_col = 0

    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val > max_val:
                max_val = val
                max_row = i
                max_col = j
    return max_val, max_row, max_col


def swap_rows(matrix, row1, row2):
    """
    Меняет местами две строки в матрице.

    Args:
        matrix: Двумерный список (список списков), представляющий матрицу.
        row1: Индекс первой строки.
        row2: Индекс второй строки.
    """
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]


def swap_columns(matrix, col1, col2):
    """
    Меняет местами два столбца в матрице.

    Args:
        matrix: Двумерный список (список списков), представляющий матрицу.
        col1: Индекс первого столбца.
        col2: Индекс второго столбца.
    """
    for row in matrix:
        row[col1], row[col2] = row[col2], row[col1]


def rearrange_matrix(matrix):
    """
    Переставляет строки и столбцы матрицы так, чтобы наибольший элемент оказался
    в левом верхнем углу.

    Args:
        matrix: Двумерный список (список списков), представляющий матрицу.

    Returns:
        Модифицированная матрица.
    """
    if not matrix:
        return matrix  # Возвращаем пустую матрицу, если она пуста
    
    max_val, max_row, max_col = find_max_element_and_its_position(matrix)

    if max_row is not None:
        swap_rows(matrix, 0, max_row)
        swap_columns(matrix, 0, max_col)

    return matrix

# Функция для ввода матрицы с клавиатуры
def get_matrix_from_input():
  """
    Получает матрицу от пользователя из ввода с клавиатуры.

    Returns:
        Двумерный список, представляющий матрицу, или None в случае ошибки.
    """
  try:
    n = int(input("Введите количество строк матрицы (n): "))
    m = int(input("Введите количество столбцов матрицы (m): "))
    
    if n <= 0 or m <=0:
         print("Ошибка: Количество строк и столбцов должно быть положительным целым числом.")
         return None
    
    matrix = []
    print("Введите элементы матрицы построчно:")
    for _ in range(n):
        row_input = input().strip()
        row = list(map(float, row_input.split()))
        if len(row) != m:
            print("Ошибка: В каждой строке должно быть m элементов.")
            return None
        matrix.append(row)
    
    return matrix
  
  except ValueError:
    print("Ошибка: Введите целое число для количества строк и столбцов матрицы и вещественные числа для элементов матрицы.")
    return None
  

# Основная часть программы:
matrix = get_matrix_from_input()

if matrix is not None:
  rearranged_matrix = rearrange_matrix(matrix)
  print("Преобразованная матрица:")
  for row in rearranged_matrix:
      print(*row)  # Вывод элементов строки через пробел