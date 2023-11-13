user_input = input("Введите числа, разделенные запятой: ")
numbers = [int(x.strip()) for x in user_input.split(',')]
num_list = numbers
num_tuple = tuple(numbers)
print("Список:", num_list)
print("Кортеж:", num_tuple)