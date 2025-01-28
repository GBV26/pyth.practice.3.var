# 5 практическая, 3 вариант
def find_largest_power_of_two(n):
    """
    Находит наибольшую целую степень двойки, не превосходящую n.

    Args:
        n: Натуральное число.

    Returns:
        Кортеж (power, result): Показатель степени и сама степень двойки.
    """
    if n <= 0:
        return None  # Обработка некорректного ввода

    power = 0
    result = 1
    while result * 2 <= n:
        result *= 2
        power += 1
    return power, result

# Получение ввода от пользователя
try:
    n = int(input("Введите натуральное число N: "))
    if n <= 0:
      print("Ошибка: N должно быть натуральным числом (больше 0).")
    else:
        power, result = find_largest_power_of_two(n)
        print(f"Показатель степени: {power}, Степень двойки: {result}")

except ValueError:
    print("Ошибка: Введите целое число.")