"""
Hàm Set difference_update trong python xóa các phần tử tồn tại trong cả
2 set1 và set 2
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "amazon", "apple"}

set1.difference_update(set2)

print(set1)
print(set2)
