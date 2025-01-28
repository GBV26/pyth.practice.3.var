# 8 практическая, 3 вариант, задание 1
import math

def calculate_hypotenuse(cathetus1, cathetus2):
    """
    Вычисляет длину гипотенузы прямоугольного треугольника по двум катетам.

    Args:
        cathetus1: Длина первого катета.
        cathetus2: Длина второго катета.

    Returns:
        Длина гипотенузы.
    """
    return math.sqrt(cathetus1**2 + cathetus2**2)

def compare_hypotenuses(cathetus1_1, cathetus2_1, cathetus1_2, cathetus2_2):
    """
    Вычисляет длины гипотенуз двух треугольников и сравнивает их.

    Args:
        cathetus1_1: Длина первого катета первого треугольника.
        cathetus2_1: Длина второго катета первого треугольника.
        cathetus1_2: Длина первого катета второго треугольника.
        cathetus2_2: Длина второго катета второго треугольника.

    Returns:
        None. Выводит результат сравнения на экран.
    """
    hypotenuse1 = calculate_hypotenuse(cathetus1_1, cathetus2_1)
    hypotenuse2 = calculate_hypotenuse(cathetus1_2, cathetus2_2)

    print(f"Гипотенуза первого треугольника: {hypotenuse1:.2f}")
    print(f"Гипотенуза второго треугольника: {hypotenuse2:.2f}")

    if hypotenuse1 > hypotenuse2:
        print("Гипотенуза первого треугольника больше.")
    elif hypotenuse1 < hypotenuse2:
        print("Гипотенуза второго треугольника больше.")
    else:
        print("Гипотенузы равны.")


# Получение ввода от пользователя:
try:
    cathetus1_1 = float(input("Введите длину первого катета первого треугольника: "))
    cathetus2_1 = float(input("Введите длину второго катета первого треугольника: "))
    cathetus1_2 = float(input("Введите длину первого катета второго треугольника: "))
    cathetus2_2 = float(input("Введите длину второго катета второго треугольника: "))

    if cathetus1_1 <= 0 or cathetus2_1 <= 0 or cathetus1_2 <=0 or cathetus2_2 <=0:
      print("Ошибка: Длины катетов должны быть положительными.")
    else:
      compare_hypotenuses(cathetus1_1, cathetus2_1, cathetus1_2, cathetus2_2)

except ValueError:
    print("Ошибка: Введите числовые значения для длин катетов.")