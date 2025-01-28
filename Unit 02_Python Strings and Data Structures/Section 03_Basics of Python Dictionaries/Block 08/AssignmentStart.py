# Assignment 1
book = {
    "title": "To Kill A Mockingbird",
    #TODO: add an author Key Value Pair
    #TODO: also a publishing year
    "available" : True
}

#TODO: add a genre key value pair for the book
#TODO: update the availablility status

# Assignment 2
grades = {
    "a" : 70,
    "b" : 80,
    "c" : 90,
}

sum = 0
for value in grades.values():
    #TODO: add the value to the sum
    pass #TODO:  remove when done.

number_of_grades = len(grades)
#TODO: figure out the average and print :)


# Assignment 3

students = {
    "Johnnie" : {"English" : 73, "Math" : 85},
    "Susie" : {"English": 80, "Math" : 90, "Science": 82}
    #TODO: add 3 more students.
}

def add_student(name, grades_to_add):
    students[name] = grades_to_add

add_student("Horatio", {"English" : 73, "Math" : 85})
#TODO: call 3 more times with new students