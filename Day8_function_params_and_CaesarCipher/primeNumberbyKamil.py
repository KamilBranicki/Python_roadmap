#Write your code below this line 👇
def prime_checker(number):
    prime = True
    for i in range (1,number+1): #niepotrzebnie taki zakres, lepszy (2,number) to wtedy nie jest potrzebny if na sprawdzanie czy 1 czy number, bez sensu Kamil
        if number % i == 0:
            if i != 1 and i !=number:
                prime = False
    if prime == False:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
