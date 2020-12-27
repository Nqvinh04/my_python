"""
Hàm Set issubset() trong Python trả về true nếu tất cả
các phần tử trong một set tồn tại trong set2, ngược lại trả về false.
"""

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)