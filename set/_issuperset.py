"""
Hàm Set issuperset() trong Python trả về true nếu tất cả
các phần tử trong set2 tồn tại trong một set, ngược lại trả về false.
"""

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = y.issuperset(x)

print(z)