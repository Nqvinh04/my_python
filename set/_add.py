"""
Hàm Set add() trong Python thêm một phần tử vào Set.

"""

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

# Không thêm được phần tử đã tồn tại
fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits)