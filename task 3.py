import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dict_ascending = dict(sorted(d.items(), key=operator.itemgetter(1)))
print(sorted_dict_ascending)
sorted_dict_descending = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(sorted_dict_descending)
