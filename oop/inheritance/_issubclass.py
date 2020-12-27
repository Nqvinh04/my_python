"""
Phương thức issubclass(sub, sup) được sử dụng để kiểm tra mối
quan hệ giữa các lớp được chỉ định. Nó trả về True nếu lớp thứ nhất
là lớp con của lớp thứ 2 và ngược lại là False
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

print("Derived là con của Calculation2:",
      issubclass(Derived,Calculation2))
print("Calculation1 là con của Calculation2:",
      issubclass(Calculation1,Calculation2))