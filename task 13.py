def calculate_expression(n):
    
    nn = int(str(n) * 2)
    nnn = int(str(n) * 3)

    
    result = n + nn + nnn

    return result


try:
    n = int(input("Введите целое число n: "))
    result = calculate_expression(n)
    print(f"Результат выражения n + nn + nnn для n = {n}: {result}")
except ValueError:
    print("Ошибка: Введите целое число.")