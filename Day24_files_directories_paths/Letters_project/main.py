#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("\Python\Projects\Day24\Letters_project\Input\Letters\starting_letter.txt", mode="r") as file:
    string_list = file.readlines()

with open(r"C:\Python\Projects\Day24\Letters_project\Input\Names\invited_names.txt", mode="r") as names_file:
    names_list = names_file.readlines()

for name in names_list:
    stripped_name = name.strip("\n")
    names_list[names_list.index(name)] = stripped_name

new_beginings = []
for i in range(0, len(names_list)):
    new_string = string_list[0].replace("[name]", names_list[i])
    new_beginings.append(new_string)

for name in names_list:
    with open(f"C:\Python\Projects\Day24\Letters_project\Output\ReadyToSend\{name}.txt", mode="w") as new_file:
        new_file.write(new_beginings[(names_list.index(name))])
        for i in range (1,len(string_list)):
            new_file.write(string_list[i])
