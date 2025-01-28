# 6 практическая, 3 вариант
def remove_dots_and_count(sentence):
  """
  Удаляет точки из строки и подсчитывает количество удаленных символов.

  Args:
    sentence: Строка, в которой нужно удалить точки.

  Returns:
    Кортеж из двух элементов:
      - Строка без точек.
      - Количество удаленных точек.
  """
  count = sentence.count('.')
  new_sentence = sentence.replace('.', '')
  return new_sentence, count

# Ввод строки
sentence = input("Введите строку: ")

# Удаление точек и подсчет
new_sentence, count = remove_dots_and_count(sentence)

# Вывод результата
print("Строка без точек:", new_sentence)
print("Количество удаленных точек:", count)
