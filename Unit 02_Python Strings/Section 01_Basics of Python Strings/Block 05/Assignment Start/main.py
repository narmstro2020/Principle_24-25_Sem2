# Assignment 1
string = input("Enter some text: ")
string = string.upper()
string = string.replace(" ", "_")
print(f"The modified string is {string}.")
print(f"The length of the modified string is {len(string)}.")

#Assignment
#string = user input value asking for some text.
#string = the upper cased copy of the string (or lower case your choice)
#string = replace " " with ""
reverse = string[::-1]
# check if string == reverse.  if so print The string is a palindrome
# if not print The string is not a palindrome.