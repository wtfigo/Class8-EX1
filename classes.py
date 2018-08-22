class animal():
    count=0
    type = ''
    ears = 0
    tail = 0
    name = ''
    sound = 'null'

    def __init__(self, type, name, ears, tail):
        self.type = type
        self.ears = ears
        self.tail = tail
        self.name = name
        animal.count +=1

    def makeSound(self):
        if self.animal.sound =='Null':
            return 'Dookie'
        else:
            return self.animal.sound

    def CallAnima(self):
        for ani in self.animal:
            Asound = animal.makeSound(self)
            print("The {} is named {} and makes", animal.type, animal.name)

class dog(animal):
    def __int__(self, name, ears, tail):
        animal.sound = 'Woof'
        animal.type = 'dog'
class cat(animal):
    def __int__(self, name, ears, tail):
        animal.sound = 'Miaau'
        animal.type = 'cat'
class garfolo(animal):
    def __int__(self, name, ears, tail):
        animal.sound = 'Woot'
        animal.type = 'garfolo'

whoopie=dog('whoopie', 1, 2)
mitzie=cat('mitzie', 3, 4)
hookie=garfolo( 'hookie', 24, 66)
moti=animal('Hoot', Moti, 2, 1)
animal.CallAnima()