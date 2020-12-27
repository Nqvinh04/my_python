"""
Hàm List insert() trong python chèn đối tượng obj vào trong list
tại chỉ số index đã cho. Hàm này không trả về bất ký giá trị nào
nhưng nó chèn phần tử đa xchp tại chỉ mục đã xác định
"""

list1 = ['java', 'python', 'c++', 'php', 'sql']
list1.insert(3, 'android')
print ("List sau khi duoc chen them doi tuong 'android': ", list1)


# List sau khi duoc chen them doi tuong 'android':
#     ['java', 'python', 'c++', 'android', 'php', 'sql']