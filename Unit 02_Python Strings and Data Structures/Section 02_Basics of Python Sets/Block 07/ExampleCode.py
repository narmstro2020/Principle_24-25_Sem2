set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # or set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

intersection_set = set1 & set2  # or set1.intersection(set2)
print(intersection_set)  # Output: {3}

difference_set = set1 - set2  # or set1.difference(set2)
print(difference_set)  # Output: {1, 2}difference_set = set1 - set2  # or set1.difference(set2)
print(difference_set)  # Output: {1, 2}

sym_diff_set = set1 ^ set2  # or set1.symmetric_difference(set2)
print(sym_diff_set)  # Output: {1, 2, 4, 5}