#Assignment 1
library_book = {
    "title" : "To Kill a Mockingbird",
    #TODO: author, year
    "available" : True
}

#library_book[#Key Here] = #Updated Value Here which is False
library_book["genre"] = "Fiction"
print(library_book)

#Assignment 2
data = {"John" : 67, "Jill" : 84, }  # add four more key value pairs
sum = 0
for value in data.values():
    #add value to sum
    pass # remove pass when done

amount = len(data)
average = sum / amount
print(f"Average is {average}")


#Assignment 3
students = {
    "Alice" : {"Math" : 85, "English": 90},
    "Bob" : {"Math" : 70, "English": 95, "Spanish" : 87},
    #Add 3 more students with fake grades in rando subjects.
}

def add_student(name, grades):
    students[name] = grades

add_student("Charlie", {"Math" : 95, "English" : 90})
print(students)





