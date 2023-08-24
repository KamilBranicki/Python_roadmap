num_char = len(input("What is your name? "))
# print("Your name has " + num_char + " characters.") - type error, dodawanie string do int nie ma sensu wiec nie działa

print(type(num_char))

new_num_char = str(num_char)

print(type(new_num_char))

print("Your name has " + new_num_char + " characters.")