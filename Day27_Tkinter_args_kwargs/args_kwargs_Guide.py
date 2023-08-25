def add(*args): #args to tuple
    result = 0
    for n in args:
        result +=n
    print(result)


add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def calculate(n, **kwargs):
    print(kwargs) #kwargs to jest dict
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5) # wynik to 25


class Car:
    def __init__(self, **kw):
        # self.make = kw["make"] - error jak nie użyje się tego atrybutu
        self.make = kw.get("make") #dzięki get() jak nie użyjemy atrybutu to zwróci nam None
        self.colour = kw.get("colour")
        self.model = kw.get("model")

my_car = Car(make="Ford", model = "Focus")
print(my_car.make)