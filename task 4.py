dict_a = {2: 10, 2: 20}
dict_b = {3: 50, 4: 40}
dict_c = {5: 70, 6: 60}

merged_dict = {}

merged_dict.update(dict_a)
merged_dict.update(dict_b)
merged_dict.update(dict_c)

print(merged_dict)