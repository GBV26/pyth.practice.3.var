# 7 практическая, 3 вариант, задание 1
def calculate_sum_of_odd_indexed_elements(arr):
    """
    Вычисляет сумму элементов с нечетными индексами в одномерном числовом массиве.

    Args:
        arr: Одномерный числовой массив.

    Returns:
        Кортеж (arr, sum_of_odd_indexed) - исходный массив и сумма элементов с нечетными индексами.
    """
    sum_of_odd_indexed = 0
    for i in range(1, len(arr), 2): # Итерируемся по нечетным индексам (начиная с 1)
        sum_of_odd_indexed += arr[i]
    return arr, sum_of_odd_indexed

# Получение ввода от пользователя (пример):
try:
  input_str = input("Введите элементы массива через пробел: ")
  arr = list(map(int, input_str.split()))  # Преобразуем строку в список целых чисел
  
  if not arr: # Проверка, что массив не пустой
     print("Ошибка: Массив не должен быть пустым.")
  else:
    d, sum_odd = calculate_sum_of_odd_indexed_elements(arr)
    print("Массив D:", d)
    print("Сумма элементов с нечетными индексами:", sum_odd)

except ValueError:
    print("Ошибка: Введите целые числа через пробел.")