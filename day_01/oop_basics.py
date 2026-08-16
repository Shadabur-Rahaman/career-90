# class Animal:
#     def __init__(self,animal,breed):
#         self.animal = animal
#         self.breed = breed
#     def bark(self):
#         print("Woof")
#     def display(self):
#         print('Name: '+self.animal+' Breed: '+self.breed)
# a1 = Animal('Dog','Golden Retriever')
# a1.bark()
# a1.display()

class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    def Sound(self):
        print(self.brand,self.year,'Booooom',)
c1 = Car('BMW',2005)
c2 = Car('Mercedez',2024)
c1.Sound()
c2.Sound()