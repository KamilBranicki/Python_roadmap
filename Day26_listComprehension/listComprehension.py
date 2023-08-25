numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)


# ->

new_list = [n + 1 for n in numbers]
print(new_list)

name = "Kamil"
new_name = [letter for letter in name]
print(new_name)

new_range = [n * 2 for n in range(1,5)]
print(new_range)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) == 4]
print(short_names)

longer_names = [name.upper() for name in names if len(name) >=5 ]
print(longer_names)