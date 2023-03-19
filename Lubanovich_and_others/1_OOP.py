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

# class Person():
#     def __init__(self, name, test_name):
#         self.name = name
#         self.test_name = test_name


# class EmailPerson(Person):
#     def __init__(self, name, email, test_name):
#         super().__init__(name, test_name)
#         self.email = email

# kok = Person('kok', 'test1')
# bob = EmailPerson('Bob', 'bla@gmail.com', 'test')
# # 
# print(bob.name)
# print(bob.email)
# print(bob.test_name)
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

# str1 = '2020-12-11 10:44:41.635'

# str2 = str1[11:16]

# print(str2)



# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def add(self, number):
#         real = self.real + number.real
#         imag = self.imag + number.imag
#         result = Complex(real, imag)
#         return result







# n1 = Complex(5, 6)
# n2 = Complex(-4, 2)

# result =  n1.add(n2)

# print(result)

# # print(result.real)
# # print(result.imag)


# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def perimeter(self):
#         return self.a + self.b + self.c
 

# triag = Triangle(5,5,5)

# print(triag.perimeter())




class Polygon:
    def __init__(self, sides):
        self.sides = sides

    
    def display_info(self):
        print('A polygon is two dimensional shape with straight lines')


    def get_perim(self):
        perim = sum(self.sides)
        return perim
    
class Triangle(Polygon):
    def display_info(self):
        print('A triangle is a polygon with 3 edges')

        super().display_info()



class Quad(Polygon):
    def display_info(self):
        print('Quad is a polygon with 4 edges')


t1 = Triangle([5,6,7])

perimeter = t1.get_perim()

print(perimeter)


t1.display_info()
        
    







