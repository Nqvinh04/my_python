"""
Hàm Set remove() trong Python xóa phần tử được chỉ định từ một set.
------------------------------------------------------------------
Hàm này khác với hàm discard(), bởi vì hàm remove() sẽ phát sinh
 lỗi nếu phần tử được chỉ định xóa không tồn tại,
 còn hàm discard() thì không phát sinh lỗi.
"""

fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)