print("welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is you age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 & age <= 55:
        bill = 0
    else:
        bill = 12
        print("Adlut tickets are $12")
    photo = input("Do you want a photo taken? Y or N.")
    if photo == "Y":
        bill += 3
    print(f"Your final bill is {bill}")
else: 
    print("Sorry, you are too little")