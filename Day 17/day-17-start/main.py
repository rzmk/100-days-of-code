class User:
    
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "mueez")
# user_1.id = "001" # like self.id in init function, but just for this user_1 object if not in init
# user_1.username = "mueez"
user_2 = User("002", "another_user")
user_1.follow(user_2)
print(user_1.followers)
print(user_2.followers)
print(user_1.following)
print(user_2.following)
