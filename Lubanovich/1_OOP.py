# from tkinter.messagebox import YESNO


# class Car:
#     def exclaim(self):
#         print('I am Car class')

# class Yugo(Car):
#     # pass
#     def exclaim(self):
#         print('I am Yugo class')
#     def need_a_push(self):
#         print('2nd method of Yugo class')
    

# yugo = Yugo()

# yugo.exclaim('Car')




    

# print(issubclass(Yugo, Car))

# car = Car()
# car.exclaim()
# yugo = Yugo()
# yugo.exclaim()
# yugo.need_a_push()

class Person():
    def __init__(self, name, test_name):
        self.name = name
        self.test_name = test_name


class EmailPerson(Person):
    def __init__(self, name, email, test_name):
        super().__init__(name, test_name)
        self.email = email

kok = Person('kok', 'test1')
bob = EmailPerson('Bob', 'bla@gmail.com', 'test')
# 
print(bob.name)
print(bob.email)
print(bob.test_name)
# print(kok.name)



# class Animal:
#     def says(self):
#         return 'I speak!'

# class Horse(Animal):
#     def says(self):
#         return 'Neigh!'

# class Donkey(Animal):
#     def says(self):
#         return 'Hee-haw!'

# class Mule(Donkey, Horse):
#     pass

# class Hinny(Horse, Donkey):
#     pass


# print(Mule.mro())


# page 205 proceed

