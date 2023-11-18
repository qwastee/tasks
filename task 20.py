# Исходный список 
numbers = [300, 18, 75, 45, 60, 91, 120]
result = list(filter(lambda x: x % 15 == 0, numbers))
print("Числа, делимые на 15:", result)