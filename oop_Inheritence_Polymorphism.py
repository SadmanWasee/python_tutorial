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

    def __init__(self):
        Animal.__init__(self)#Invoking the super class
        print("Dog Created")


        