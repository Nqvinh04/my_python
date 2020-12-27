"""
Phương thức isinstance () được sử dụng đề kiểm tra mối quan hệ giữa các
đối tượng và các lớp. Nó trả về True nếu tham số đầu tiên, tức là Object
là thể hiện của tham số thứ hai, tức là lớp
"""


class Calculation1:
    def Summation(self, a, b):
        return a + b

class Calculation2:
    def Multiplication(self, a, b):
        return a * b


class Derived(Calculation1, Calculation2):
    def Divide(self, a, b):
        return a / b


d = Derived()
c2 = Derived()
C2 = Calculation2()
print("Đối tượng d là thể hiện của lớp Derived: ",
      isinstance(d, Derived))

print("Đối tượng d là thể hiện của lớp Derived: ",
      isinstance(C2, Calculation2))


print("Đối tượng d là thể hiện của lớp Derived: ",
      isinstance(c2, Calculation2))
