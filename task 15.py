def find_unique_elements(list1, list2):
    unique_elements = [element for element in list1 if element not in list2]
    return unique_elements


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = find_unique_elements(list1, list2)

print("Элементы из первого списка, которых нет во втором:")
print(result)