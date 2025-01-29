# 4 практическая, 3 вариант
def print_odd_numbers_desc(a, b):
    """
    Выводит все нечетные числа от a до b включительно в порядке убывания.
    Args:
        a: Целое число (начало диапазона), a > b.
        b: Целое число (конец диапазона).

    Raises:
        ValueError: Если a <= b.
    """
    if a <= b:
        raise ValueError("A должно быть больше B.")
    for i in range(a, b - 1, -1):
        if i % 2 != 0:
            print(i, end=" ")
    print()  # Переход на новую строку после вывода всех чисел
if __name__ == '__main__':
    try:
        a = int(input("Введите целое число A: "))
        b = int(input("Введите целое число B: "))
        print_odd_numbers_desc(a, b)
    except ValueError as e:
        print(f"Ошибка: {e}")
