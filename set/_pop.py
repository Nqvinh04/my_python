"""
Hàm Set pop() trong Python xóa phần tử cuối cùng của một set.
Nhưng vì set là không có thứ tự nên hàm pop() sẽ xóa
ngẫu nhiên một phần tử của set.
"""

fruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits)