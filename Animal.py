class Animal:
    def __init__(self, name, hungry = True, thirsty = True, needtopoop = True, dirty = True): 
        self.__name = name
        self.__hungry = hungry
        self.__thristy = thirsty
        self.__needtopoop = needtopoop
        self.__dirty = dirty
        print("hello i am", self.__name)
        print("I want to go on a walk. I am hungry. I want to jump. I need to use the bathroom")

    def talk(self):
        print("hi")

    def walk(self):
        print("*steps forward*")

    def eat(self):
        self.__hungry = False
        print("*chomp*")

    def drink(self):
        self.__thirsty = False
        print("*drinks water*")

    def poop(self):
        self.__needtopoop = False
        print("*bowels emptied*")

    def bathe(self):
        self.__dirty = False
        print("All clean now")

    def status(self):
        print(self.__name, f''' is hungry? {self.__hungry}. is thirsty? {self.__thristy}. needs to poop? {self.__needtopoop}. is dirty? {self.__dirty}''')
