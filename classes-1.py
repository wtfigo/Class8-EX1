class Animal(object):
    name = None
    sex = None
    age = -1

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def make_sound(self):
        return None

class dog(Animal):
   def make_sound(self):
       return "Woof!"

class cat(Animal):
   def make_sound(self):
       return "mioooo!"

class lion(Animal):
   def make_sound(self):
       return "aaaaaaaaaaa!"

boni=dog("boni","male",3)
mizi=cat("mizi","female",2)
king=lion("king","male",4)
animals=[boni,mizi,king]
for ani in animals:
    print("the sound is %s"%ani.make_sound())

