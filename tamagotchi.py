"""A Tamagotchi Game"""
from random import randrange

class Pet:
    # Class object attribute
    # Same for any instance of a class
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Wolf']

    #Method called upon when creating an instance of a class
    def __init__(self,name = 'Dog', age = 0):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute name
        self.name = name
        self.age = age
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class



    def clock_tick(self):
        self.age + 0.25
        self.hunger += 1
        self.borebom += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "Happy"
        else:
            return "Bored"

    # STATE
    def __str__(self):
        state = " I'm " + self.name + "."
        state = " I feel " + self.mood() + "."
        # state += "Hunger {} Boredom {} Words {}".format(self.hunger, self.boredom, self.sounds)
        return state

    # OPERATIONS/Actions ----> Methods

    def bark(self):
         print("WOOF! My name is {}".format(self.name))

    def sleep(self):
        print("WOOF! My name is {}".format(self.name))

    def wake(self):
        print("WOOF! My name is {}".format(self.name))


if __name__ == "__main__":
    my_pet = Pet('Nea', 8)
    my_pet.bark()
    my_pet.mood()

