# 9 практическая, 3 вариант, задание 1
def is_symmetric_matrix(matrix):
    """
    Проверяет, является ли заданная квадратная матрица симметричной
    относительно главной диагонали.

    Args:
        matrix: Двумерный список (список списков), представляющий квадратную матрицу.

    Returns:
        True, если матрица симметрична, иначе False.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):  # Итерируемся по верхней треугольной части матрицы
            if matrix[i][j] != matrix[j][i]:
                return False  # Если элемент не симметричен, возвращаем False
    return True  # Если все элементы симметричны, возвращаем True


# Функция для ввода матрицы с клавиатуры
def get_matrix_from_input():
    """
    Получает матрицу от пользователя из ввода с клавиатуры.

    Returns:
        Двумерный список, представляющий матрицу, или None в случае ошибки.
    """
    try:
        n = int(input("Введите порядок матрицы (n): "))
        if n <= 0:
            print("Ошибка: Порядок матрицы должен быть положительным целым числом.")
            return None
        
        matrix = []
        print("Введите элементы матрицы построчно:")
        for _ in range(n):
            row_input = input().strip()
            row = list(map(int, row_input.split()))
            if len(row) != n:
              print("Ошибка: В каждой строке должно быть n элементов.")
              return None
            matrix.append(row)

        return matrix
    except ValueError:
        print("Ошибка: Введите целое число для порядка матрицы и целые числа для элементов матрицы.")
        return None

# Основная часть программы:
matrix = get_matrix_from_input()

if matrix is not None:
    if is_symmetric_matrix(matrix):
        print("Матрица является симметричной.")
    else:
        print("Матрица не является симметричной.")