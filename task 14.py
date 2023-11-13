def print_even_numbers_until_237(numbers):
    for number in numbers:
        # Проверяем, чётное ли число
        if number % 2 == 0:
            print(number)
        
        # равно ли число 237
        if number == 237:
            print("Достигнуто число 237. Программа завершена.")
            break

# Пример использования
my_list = [2, 5, 10, 15, 20, 237, 40, 50, 60, 70]

print("Чётные числа из списка:")
print_even_numbers_until_237(my_list)