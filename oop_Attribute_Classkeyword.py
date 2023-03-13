class Dog(): #Creating a Dog class 
    def __init__(self,breed,name,spots): #_init_ is the constructor method for a class in python. It is called automatically when we create an instace of the class
    #self is the first parameter which represents the object itself     
        self.breed = breed
        self.name = name
        self.spots = spots

        #We take attributes as argument and assign it as self.attribute  

my_dog = Dog("German Sheperd", "Kruger", False)

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)

