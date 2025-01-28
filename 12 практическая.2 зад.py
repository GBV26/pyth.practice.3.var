def print_alternate():
    num = int(input("Введите натуральное число (0 для окончания ввода): "))
    if num == 0:
        return
    print_alternate()  