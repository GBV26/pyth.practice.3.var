# 3 практическая, 3 вариант
def calculate_time(minutes_passed):
  if minutes_passed < 0:
      return 0, 0
  total_minutes_in_day = 24 * 60 
  minutes_passed = minutes_passed % total_minutes_in_day
  hours = minutes_passed // 60
  minutes = minutes_passed % 60
  return hours, minutes
# Пример использования:
n = int(input("Введите количество минут, прошедших с начала суток: "))
hours, minutes = calculate_time(n)
print(f"Время: {hours} часов {minutes} минут")
