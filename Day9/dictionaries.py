programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
 "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing somethging over and over again"

print(programming_dictionary)

empty_dictionary = {}

#programming_dictionary = {}

programming_dictionary["Bug"] = "New value"

print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])