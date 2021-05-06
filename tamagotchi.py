"""A Tamagotchi Game"""
from random import randrange

class Pet:
    # Class object attribute
    # Same for any instance of a class
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Woof']
    type = "mammal"

    # Method called upon when creating an instance of a class
    # In this instance
    def __init__(self,name = 'Dog', age = 0):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute name
        print("PET CREATED")
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
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    # STATE
    def __str__(self):
        state = " I'm " + self.name + "."
        state = " I feel " + self.mood() + "."
        # state += "Hunger {} Boredom {} Words {}".format(self.hunger, self.boredom, self.sounds)
        return state

    # OPERATIONS/Actions ----> Methods

    # def what_am_i(self):
    #     print("I am a {}".format(type))


    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        print("My name is {} ".format(self.name) + " and right now I am " + self.mood() + ".")
        self.reduce_boredom()

    def sleep(self):
        print("WOOF! My name is {}".format(self.name))

    def wake(self):
        print("WOOF! My name is {}".format(self.name))

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)


class Dog(Pet):
    def __init__(self):
        Pet.__init__(self)
        print("Dog Created")
    def bark(self):
         print(self.sounds)
    def who_am_i(self):
        print("I am a dog!")


# class Cat:
#     def __init__(self):
#         Pet.__init__(self)
#         print("Cat Created")
#
#     def bark(self):
#         print(self.sounds)
#
#     def who_am_i(self):
#         print("I am a dog!")


if __name__ == "__main__":
    my_pet = Dog()
    # my_pet = Cat()

    my_pet = Dog()
    my_pet.bark()
    my_pet.hi()

