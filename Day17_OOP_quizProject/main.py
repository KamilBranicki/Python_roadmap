class User:
    def __init__(self, id, name): #constructor
        self.id = id
        self.username = name
        self.followers = 0
        self.following = 0
        print("new user being created...")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Kamil")
user_2 = User("002", "Olcia")

user_1.follow(user_2)
print(user_1.followers, user_1.following)
print(user_2.followers, user_2.following)
