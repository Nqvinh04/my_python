"""
Hàm Set symmetric_difference_update() trong Python cập nhật
set ban đầu bằng việc loại bỏ phần tử của cả 2 set đã cho,
sao cho các phần tử này tồn tại trong set này nhưng không
tồn tại trong set kia.
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
