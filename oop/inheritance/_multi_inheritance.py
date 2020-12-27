"""
Python cung cấp cho chúng ta sự linh hoạt để kế thừa nhiều
lớp cơ sở trong lớp con
"""

class Calculation1:
    def Sum(self, a, b):
        return a + b
class Calculation2:
    def Multi(self, a, b):
        return a * b
class Derived(Calculation1, Calculation2):
    def Divide(self, a, b):
        return a / b
d = Derived()
print(d.Sum(10, 20))
print(d.Multi(10, 20))
print(d.Divide(10, 20))