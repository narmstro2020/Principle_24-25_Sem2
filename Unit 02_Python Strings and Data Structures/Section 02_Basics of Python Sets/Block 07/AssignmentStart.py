# Assignment 1
def remove_dups(my_list):
    my_set = set(my_list)
    return list(my_set)

a_list = [1, 2, 2, 3, 4, 5, 5]
print(remove_dups(a_list))

# Assignment 2
set1 = {1, 2, 3}
set2 = {2, 3, 4}
#TODO: You can do the rest

# Assignment 3
set3 = {1, 2, 3, 4, 5}
element_to_find = 3
element_found = False
for element in set3:
    #TODO: check if element_to_find is equal to element
    #TODO: if so set element_found to True
    #TODO: break out of the for loop
    pass #TODO: remove this pass when done.

if element_found:
    print(f"Element {element_to_find} found in the set")
else:
    print(f"Element {element_to_find} not found in the set")
