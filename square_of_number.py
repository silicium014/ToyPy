a = -1
while a != 0:
    try:
        a = int(input("Введите число и получите его квадрат.\n"))
    except ValueError as er:
        print("Введите целое число!")
        continue
    assert(a>=0)
    print(a**2)
    print("Для выхода введите: 0")