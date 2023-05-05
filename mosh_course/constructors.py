class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10,20)
point.x = 11
print(point.x)
print(point.y)

class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        if self.name == "James Bond":
            print(f"The name is Bond, {self.name}")
        else:
            print(f"Hi, I am {self.name}")


bob = Person("Robert Smith")
bob.talk()

jim = Person("James Bond")
jim.talk()