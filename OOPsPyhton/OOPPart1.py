class Sample:
    x =50
x = Sample()
print(type(x))

class Dog():
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF THE CLASS
    species = 'Mammmal'

    def __init__(self,breed,name):
        #Attribute
        #We take an argument
        #Assign it using self.attridute_name
        self.breed = breed
        self.name = name
    def bark(self):
        print("woof! My name is {}".format(self.name))

dog = Dog('Huski','Sam')
print(dog.breed,dog.name)
print(dog.bark())