"""
Hàm Set discard() trong Python xóa phần tử được chỉ định từ một set.
-------------------------------------------------------------------
Hàm này khác với hàm remove(), bởi vì hàm remove() sẽ phát sinh lỗi nếu
phần tử được chỉ định không tồn tại, còn hàm discard thì sẽ không phát
sinh lỗi
"""

fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits)
