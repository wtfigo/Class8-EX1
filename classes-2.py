class Animal(object):
    name = None
    type = None
    sound = None

    def __init__(self, name, type, sound):
        self.name = name
        self.Type = type
        self.sound = sound

    def  make_sound (self):
                return (self.sound)

class dogs(Animal):

    def __init__(self, type="dog", sound="woof"):
        self.Type = type
        self.sound = sound

class cats(Animal):

    def __init__(self, type="cat", sound="miao"):
        self.Type = type
        self.sound = sound

pickatzu = Animal('pickatzu','pockemon','pika')
honey = dogs("honey")
oscar = cats("Oscar")


my_animals = [pickatzu,honey,oscar]

for animal in my_animals:
    print(animal.make_sound())