"""
Hàm Set symmetric difference() trong python trả về một set mà chứa
các phần tử của cả 2 set đã cho, sao cho các phần tử này tồn tại
trong set này nhưng không tồn tại trong set kia
"""


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

# Kết quả: trả về Set chứa phần từ không trùng lặp ở 2 set đã cho
# {'google', 'microsoft', 'cherry', 'banana'}