
numbers1 = [10, 2, 3, 4, 51, 6, 75, 8, 91]
numbers2 = [10, 2, 3, 4, 51, 2, 75, 85, 91]

are_all_unique = lambda sequence: len(set(sequence)) == len(sequence)
result1 = are_all_unique(numbers1)
result2 = are_all_unique(numbers2)
print("Все числа уникальны:", result1, result2)
