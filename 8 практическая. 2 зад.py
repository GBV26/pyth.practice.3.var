# 8 практическая, 3 вариант, задание 2
def sort_letters_in_words(text):
    """
    Сортирует буквы в каждом слове строки по алфавиту.

    Args:
        text: Входная строка.

    Returns:
        Строка, в которой буквы каждого слова отсортированы по алфавиту.
    """
    words = text.split()  # Разделяем строку на слова
    sorted_words = []
    for word in words:
        sorted_word = "".join(sorted(word))  # Сортируем буквы и соединяем обратно
        sorted_words.append(sorted_word)
    return " ".join(sorted_words)  # Соединяем слова обратно в строку

# Получение ввода от пользователя:
try:
    text = input("Введите строку: ")
    result = sort_letters_in_words(text)
    print("Преобразованная строка:", result)
except Exception as e:
    print(f"Ошибка при обработке ввода: {e}")