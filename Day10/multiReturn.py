

def function (name1, name2):
    """Take a first and last name and format it 
    to return the title case version of the name.""" #docstring
    if name1 == "" or name2 =="":
        return "You didn't provide valid inputs."
    formated_name1 = name1.title()
    formated_name2 = name2.title()
    return f"{formated_name1} {formated_name2}"

print(function(input("What is your first name? "), input("What is your last name? ")))