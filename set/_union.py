"""
Hàm Set union() trong Python trả về một set chứa tất cả
các phần tử của set đã cho và tất cả các phần tử của các
set được chỉ định.
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)