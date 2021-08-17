x =25
def my_fun ():
    x =50
    return x
print (x)
print(my_fun())

lambda x: x**2

name = "this is global name"

def greet():
    name = "sammy"
    def hello():
        print("Hello "+name)
    hello()

greet()

x = 50
def func(x):
    print("x is:",x)
    x=1000
    print("local x xhnage to: ",x)
func(x)
print(x)
mylist = {'key1': 'value','key2': 'what'}
print(type(mylist))

class Myclass():
    pass

x = Myclass()
print(type(x))


class Dog():
    # CLASS OBJECT AtTRIBUTE

    species = "Mammal"

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

mydog = Dog(breed= "Lab", name="Arpit")
otherdog = Dog(breed="Huskie", name="pankaj")
print(mydog.breed, mydog.name, mydog.species)
print(otherdog.breed, mydog.name, mydog.species)

class Circle():
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius*Circle.pi

    def set_radius(self,new_ra):
        self.radius = new_ra

myc = Circle(3)
print(myc.radius)
print(myc.area())
myc.set_radius(10)
print(myc.radius)
print(myc.area())


class Animal():

    def __init__(self):
        print("Animal Class")

    def whoami(self):
        print('Animal')

    def eat(self):
        print('Eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')

    def bark(self):
        print('Woof')

    def eat(self):
        print('Dog Eating')


mya = Dog()
mya.whoami()
mya.eat()
mya.bark()

myb = Animal()
myb.whoami()
myb.eat()


class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {},Author: {},Pages: {}".format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

p = Book('Python','Vaibhav',200)
print(len(p))