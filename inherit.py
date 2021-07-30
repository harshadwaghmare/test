#!/usr/bin/python
class Greet:
    def __init__(self) -> None:
        pass
    def greet (self):
        return input("Enter greetings : ")

g = Greet()
print ("Your greetings : " + g.greet())