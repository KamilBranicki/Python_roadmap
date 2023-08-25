#Local Scopre
def increase_enemies():
    enemies = 2
    print(enemies)

increase_enemies()
#print(enemies)

#Global Scope
teammates = 4

def team():
    print(teammates)

team()

#There is no Block Scope for example in if

#Modifying Global Scope, but avoid it.
global_count = 1

def change_count():
    global global_count
global_count += 1

change_count
print(global_count)

#Instead og modifying, return new value

def correct_change_global():
    return global_count + 1

print(correct_change_global())

#Global variables are perfect for global constants
#you can use uppercase to remind yourself to not modify these variables
PI = 3.14159
URL = "https://www.google.pl/"

