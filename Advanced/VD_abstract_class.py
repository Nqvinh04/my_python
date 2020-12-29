from abc import ABC, abstractmethod

class PersonAbstract(ABC):
    name = None
    age = 0
    def getName(self):
        print(self.name)
    def getAge(self):
        print(self.age)
    @abstractmethod
    def getFull(self):
        pass

class Person(PersonAbstract):
    name = 'Vu Thanh Tai'
    age = 22
    def getFull(self):
        self.getName()
        self.getAge()

Person().getFull()
