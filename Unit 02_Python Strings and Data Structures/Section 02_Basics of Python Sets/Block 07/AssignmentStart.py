#Assignment 1
def remove_dups(the_list):
    unique_set = set(the_list)
    return list(unique_set)

my_list = [1, 2, 3, 3, 4, 5, 5]
print(remove_dups(my_list))

#Assignment 2
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)


#Assignment 3
set3 = {1, 2, 3, 4, 5}
element_to_find = 6
element_found = False
for element in set3:
    #TODO: Check if element is equal to element to find
    #TODO: set element_found to True
    #TODO: break out of the loop
    pass #TODO: remove this pass when done.

if element_found:
    print(f"The element {element_to_find} was found")
else:
    print(f"The element {element_to_find} was not found")





