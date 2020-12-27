"""
Hàm Set intersection_update() trong Python loại bỏ các phần tử
mà không tồn tại trong cả hai hoặc nhiều set.
--------------------------------------------------------------
Hàm intersection_update() khác với hàm intersection(),
bởi vì hàm intersection() trả về một set mới,
còn hàm intersection_update() loại bỏ các phần tử các phần tử
không tồn tại từ các set ban đầu.
"""
x = {"apple", "banana", "cherry"}
y = {"google", "amazon", "apple"}

x.intersection_update(y)

print(x)
