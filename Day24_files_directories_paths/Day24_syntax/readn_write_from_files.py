file = open("my_file.txt")
contents = file.read()
print(contents)
file.close() #trzeba zamknąć aby zwolnić resource pc

#lub
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text")

with open("new_file.txt", mode="w") as file:
    file.write("New text")


