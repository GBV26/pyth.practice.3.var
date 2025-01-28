# 7 практическая, 3 вариант, задание 2
def modify_array(arr):
    """
    Заменяет все элементы массива, меньшие 15, их удвоенными значениями.

    Args:
        arr: Одномерный массив целых чисел.

    Returns:
        Модифицированный массив.
    """
    modified_arr = []
    for element in arr:
        if element < 15:
            modified_arr.append(element * 2)
        else:
            modified_arr.append(element)
    return modified_arr

# Пример использования с вводом от пользователя:
try:
    input_str = input("Введите 8 элементов массива через пробел: ")
    arr = list(map(int, input_str.split()))

    if len(arr) != 8:
        print("Ошибка: Введите ровно 8 элементов.")
    else:
        modified_arr = modify_array(arr)
        print("Преобразованный массив:", modified_arr)

except ValueError:
    print("Ошибка: Введите целые числа через пробел.")