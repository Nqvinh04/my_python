"""
Để khai báo được một abstract class trong Python, thì class này bắt buộc phải được kế thừa từ
một ABC (Abstract Base Classes ) của Python
"""
from abc import ABC, abstractmethod
class PersonAbstract(ABC):
    name = None
    age = 0
    def getName(self):
        print(self.name)
    def getAge(self):
        print(self.age)

"""
Khai báo phương thức abstract trong Python 
"""
from abc import ABC, abstractmethod
class ClassName(ABC):
    @abstractmethod
    def methodName(self):
        pass
