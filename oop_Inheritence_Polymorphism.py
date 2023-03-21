class Animal():
    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am animal")

    def eat(self):
        print("I am eating")

my_animal = Animal()
my_animal.eat()

#Dog is now a derieved class by inheriting Animal class 
class Dog(Animal):

    def __init__(self,name):
        self.name = name
        Animal.__init__(self)   #Invoking the super class
        print("Dog Created")

    #Overriding the who_am_i method in child class 
    def who_am_i(self):
        #return super().who_am_i() 
        print("I am a dog")

    def bark(self):
        print("WOOF!")

    def speak(self):
        return self.name +" says WOOF!"
    
class Cat(Animal):

    def __init__(self,name):
        self.name = name
        Animal.__init__(self)   #Invoking the super class
        print("Cat Created")

    #Overriding the who_am_i method in child class 
    def who_am_i(self):
        #return super().who_am_i() 
        print("I am a cat")

    def speak(self):
        return self.name +" says MEAW!"


inu = Dog("Inu")
inu.who_am_i() #Here the who_am_I of dog class will be invoked as this instance of the method is associated with the dog class
print(inu.speak())

neko = Cat("Neko")
print(neko.speak())



#clreating an abstract class to make it so that the genealized parent class is not invoked 
class Plant():

    def _init_(self):
        pass

    def getname(self):
        raise NotImplementedError("The functioned must be invoked from child class")
    

class Rose(Plant):
    def _init_(self):
        plant.__init__(self)

    def getname(self):
        print("My name is rose!")

plant = Plant()
#plant.getname()

rose = Rose()
rose.getname()

#Practical example of use of abstract class : Creating a class that will deal with different types of file with different methods. Sometimes we may need to reuse the same method for different child classes for example we may need the open() method for all the file formats then we can use abstract class