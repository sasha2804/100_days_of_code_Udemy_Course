'''
class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name    
    @property
    def name(self):
        print("inside getter")
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print("inside setter")
        self.hidden_name = input_name

duck1 = Duck("Howard")
print(duck1.name)

duck1.name = "Hoho"
print(duck1.name)
'''



class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("new user")
    
    def follow(self, user):
        user.followers += 1
        self.following +=1



user_1 = User("001", "Koko")
user_2 = User("002", "Jack")
user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
