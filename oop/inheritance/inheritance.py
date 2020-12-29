# class Foo:
#     name = 'Foo'
#     def getName(self):
#         print("class: Foo")
#
# class Bar(Foo):
#     name = 'Bar'
#     def getName(self):
#         # print("Class: Bar")
#         # print("Attribute name: " + super().getName())
#         super().getName()
#
# # print(Foo().name)
# # Foo().getName()
#
# # print(Bar().name)
# Bar().getName()

"""
Đa kế thừa
"""
# class Frist:
#     # def getFirst(self):
#     #     print("Class: Frist")
#     def getClass(self):
#         print("Class: Frist")
#         super().getClass()
#
# class Second:
#     # def getSecond(self):
#     #     print("Class: Second")
#     def getClass(self):
#         print("Class: Second")
#
#
# class Third(Frist, Second):
#     def getClass(self):
#         # print("Class: Third")
#         super().getClass()
# third = Third()
# # third.getFirst()
# # third.getSecond()
# # third.getThird()
# third.getClass()

"""
Bắc Cầu 
"""
class First:
    def getClass(self):
        print("Class: First")

class Second(First):
    def getClass(self):
        super().getClass()
        print("Class: Second")

class Third(Second):
    def getClass(self):
        super().getClass

third = Third()
third.getClass()
