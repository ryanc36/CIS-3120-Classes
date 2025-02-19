class Animal:
    def __init__(self, name): 
        self.__name = name
        print("hello i am", self.__name)

    def talk(self):
        print("hi")

    def walk(self):
        print("*steps forward*")

    def eat(self):
        print("*chomp*")

    def jump(self):
        print("*boing*")

    def poop(self):
        print("bowel emptied")

