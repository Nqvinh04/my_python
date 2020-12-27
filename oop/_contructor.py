# class Employee:
#     def __init__(self, name, id):
#         self.id = id
#         self.name = name
#     def display (self):
#         print("ID: %d \nName: %s" % (self.id, self.name))
#
# emp1 = Employee("Vinh", 101)
# emp2 = Employee("Trung", 102)
#
# emp1.display()
# emp2.display()
#
# class Student:
#     count = 0
#     def __init__(self):
#         Student.count = Student.count + 1
#
# s1 = Student()
# s2 = Student()
# s3 = Student()
# print("Số lượng sinh viên là: ", Student.count)

class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

# Tạo đối tượng của lớp Student
s = Student("Trung", 101, 23)

# in thuộc tính name của đối tượng s
print(getattr(s, 'name'))

# gán giá trị của age là 23
setattr(s, "age", 23)

# in giá trị của age
print(getattr(s, 'age'))

# true nếu student chứa thuộc tính id
print(hasattr(s, 'id'))

# # xóa thuộc tính age
# delattr(s, 'age')
#
# # bắn ra lỗi nếu age đã bị xóa
# print(s.age)

print(s.__doc__)
print(s.__dict__)
print(s.__module__)


