# 10 практическая, 3 вариан
import math
import os

def is_symmetric_matrix(matrix):
    """
    Проверяет, является ли заданная квадратная матрица симметричной
    относительно главной диагонали.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def find_max_element_and_its_position(matrix):
    """
    Находит наибольший элемент в матрице и его координаты.
    """
    if not matrix:
        return None, None, None

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
    """
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

def swap_columns(matrix, col1, col2):
    """
    Меняет местами два столбца в матрице.
    """
    for row in matrix:
        row[col1], row[col2] = row[col2], row[col1]

def rearrange_matrix(matrix):
    """
    Переставляет строки и столбцы матрицы, чтобы наибольший элемент оказался в верхнем левом углу.
    """
    if not matrix:
        return matrix
    
    max_val, max_row, max_col = find_max_element_and_its_position(matrix)

    if max_row is not None:
      swap_rows(matrix, 0, max_row)
      swap_columns(matrix, 0, max_col)

    return matrix


def read_matrices_from_file(filename):
    """
    Читает матрицы из файла.

    Args:
        filename: Имя файла для чтения.

    Returns:
       Список словарей, где каждый словарь содержит: тип матрицы ('symmetric' или 'general') и саму матрицу.
       Возвращает None если произошла ошибка.
    """
    matrices = []
    try:
        with open(filename, 'r') as file:
            while True:
                # Читаем тип матрицы
                line = file.readline().strip()
                if not line:
                   break
                if line not in ("symmetric", "general"):
                  print("Ошибка: Неизвестный тип матрицы. Тип матрицы должен быть 'symmetric' или 'general'.")
                  return None

                matrix_type = line

                # Читаем размеры матрицы
                line = file.readline()
                if not line:
                    print("Ошибка: Не указаны размеры матрицы.")
                    return None
                try:
                    n, m = map(int, line.split())
                    if n <=0 or m <=0:
                      print("Ошибка: Неправильный размер матрицы")
                      return None

                    matrix = []
                    for _ in range(n):
                        row_input = file.readline().strip()
                        row = list(map(float, row_input.split()))

                        if len(row) != m:
                            print("Ошибка: Неправильный формат матрицы в файле, ожидается ",m," столбцов")
                            return None
                        matrix.append(row)

                    matrices.append({"type": matrix_type, "matrix": matrix})

                except (ValueError, TypeError):
                    print("Ошибка: Неправильный формат данных в файле.")
                    return None

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return None

    return matrices


def write_results_to_file(filename, results):
    """
    Записывает результаты обработки матриц в файл.

    Args:
        filename: Имя файла для записи.
        results: Список словарей с результатами обработки матриц.
    """
    try:
        with open(filename, 'w') as file:
            for result in results:
              matrix_type = result['type']
              matrix = result['matrix']

              if matrix_type == 'symmetric':
                  is_sym = is_symmetric_matrix(matrix)
                  file.write(f"Матрица симметричная: {is_sym}\n")

              elif matrix_type == 'general':
                rearranged_matrix = rearrange_matrix(matrix)
                file.write("Преобразованная матрица:\n")
                for row in rearranged_matrix:
                    file.write(' '.join(map(str,row)) + '\n')
              file.write("\n")


    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")


# Запрос имени файла ввода у пользователя:
filename = input("Введите имя файла для ввода (ФИО_группа_vvod.txt): ")

if not filename:
   print("Ошибка: Имя файла не может быть пустым.")
else:
  # Проверка правильности расширения
  if not filename.lower().endswith('_vvod.txt'):
        print("Ошибка: Имя файла должно заканчиваться на '_vvod.txt'.")
  else:
    matrices = read_matrices_from_file(filename) # Чтение матриц из файла

    if matrices is not None:

      output_filename = filename.replace('_vvod.txt', '_vivod.txt') # Формирование имени файла вывода

      if not output_filename:
          print("Ошибка: Ошибка формирования имени файла вывода")
      else:
          write_results_to_file(output_filename, matrices) # Запись результатов в файл

          print(f"Результаты записаны в файл: '{output_filename}'")