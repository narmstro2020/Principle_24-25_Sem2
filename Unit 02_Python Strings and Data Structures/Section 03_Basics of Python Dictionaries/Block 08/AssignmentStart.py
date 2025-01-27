#Assignment 1
book = {
    "title" : "To Kill A Mockingbird",
    #TODO: author, year, available.  Available will be True or False
    #TODO: you can also use a different book.
}

#TODO: book["available"] = New value which is either True or False
#TODO: book["genre"] = "Fiction"
print(book)

#Assignment 2
class_grades = {
    "John" : 67,
    #TODO: 4 more students name, grade
}

sum = 0
for grade in class_grades.values():
    sum += grade

num_grades = len(class_grades)
#TODO: average = find the average with MATH !!!!
#TODO: print the average.


#Assignment 3
students = {
    "Alice" : {"Math" : 85, "English" : 90},
    "Bob" : {"Math" : 75, "English" : 82, "Science" : 91},
    #TODO: add 3 more students with rando names and course dictionaries
}

def add_student(name, grades):
    students[name] = grades

add_student("Charlie", {"Math" : 72, "English" : 82})
#TODO: use add_student to add 2 more students
print(students)





