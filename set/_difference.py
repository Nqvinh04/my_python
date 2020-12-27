"""
Hàm Set difference() trong Python trả về một set chứa các phần tử
tồn tại trong set 1 mà không tồn tại trong set 2
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "amazon", "apple"}

z = set1.difference(set2)

print(z)