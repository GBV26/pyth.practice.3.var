import math
# Заданные значения
x = 3.74 * 10**-2
y = -0.825
z = 0.16 * 10**2
# Вычисление значений для числителя
numerator = 1 + math.sin(x + y)**2
# Вычисление значений для знаменателя - исправленная строка
denominator = abs(x - (2.0 * y) / (1.0 + x**2 * y**2)) 
# Вычисление первого слагаемого
first_term = (numerator / denominator) * x**abs(y)
# Вычисление арктангенса
arctan_val = math.atan(1 / z)
# Вычисление второго слагаемого
second_term = math.cos(arctan_val)**2
# Вычисление общего значения s
s = first_term + second_term
# Вывод результата
print(f"s = {s:.5f}")
