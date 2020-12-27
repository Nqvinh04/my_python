"""
Hàm Set isdisjoint() trong Python trả về true nếu không có
phần tử nào trong một set trùng với phần tử nào trong set thứ 2.
Trả về false nếu có bất kỳ phần tử nào trong set ban đầu giống
với set thứ 2.
"""

x = {"apple", "banana", "cherry"}
y = {"google", "amazon", "yahoo"}

z = x.isdisjoint(y)

print(z)

# Kết quả: true