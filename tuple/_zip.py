"""
Hàm zip() trong Python trả về một đối tượng zip,
là một iterator dạng danh sách các tuple kết hợp
các phần tử từ các iterator (được tạo thành từ các iterable) khác
"""
numberList = [1, 2, 3]
strList = ['one', 'two', 'three']

result = zip()
# print(result)

resultList = list(result)
print(resultList)

result = zip(numberList, strList)
print(result)
resultSet = set(result)
print(resultSet)

