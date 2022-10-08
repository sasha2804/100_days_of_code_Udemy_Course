# class Car:
#     def exclaim(self):
#         print('I am Car class')

# class Yugo(Car):
#     def exclaim(self):
#         print('I am Yugo class')
#     def need_a_push(self):
#         print('2nd method of Yugo class')


    

# print(issubclass(Yugo, Car))

# car = Car()
# car.exclaim()
# yugo = Yugo()
# yugo.exclaim()
# yugo.need_a_push()

# class Person():
#     def __init__(self, name):
#         self.name = name

# class EmailPerson(Person):
#     def __init__(self, name, email):
#         super().__init__(name)
#         self.email = email

# kok = Person('kok')
# bob = EmailPerson('Bob', 'bla@gmail.com')

# print(bob.name)
# print(bob.email)
# print(kok.name)



class Animal:
    def says(self):
        return 'I speak!'

class Horse(Animal):
    def says(self):
        return 'Neigh!'

class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'

class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    pass


print(Mule.mro())


# page 205 proceed