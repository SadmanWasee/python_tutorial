class Dog(): 
    #Class object attribute 
    #same for any instance of a class.
    species = 'Canis familiaris'
    def __init__(self,breed,name,spots): 
        self.breed = breed
        self.name = name
        self.spots = spots
    #Method - function inside of a class that will work with the object in some way 
    def bark(self):
        print("Woof my name is {}".format(self.name))

    def dotricks(self, trick):
        print("{a} did {b}".format(a=self.name,b=trick))

        

my_dog = Dog("German Sheperd", "Kruger", False)
print(type(my_dog))
print(my_dog.species)
my_dog.bark()
my_dog.dotricks("A roll over")


class Crircle():
    #class object attribute 
    pi = 3.14

    def __init__(self,radius =1):
        self.radius = radius

    #Method
    def get_circumfarence(self):
        return (2*self.pi*self.radius)
        
my_circle = Crircle()
my_circle2 = Crircle(2)

print(my_circle.get_circumfarence())

print(my_circle2.get_circumfarence())