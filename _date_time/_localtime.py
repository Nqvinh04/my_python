"""
Hàm localtime() nhận một tham số là time.time() trả về thời gian hiện tại của hệ thống.
Trong đó time là mô-đun và time() là hàm của mô-đun time.
"""
import time
localtime = time.localtime(time.time())
print("Thoi gian hien tai la :", localtime)

localtime1 = time.asctime(time.localtime(time.time()))
print("Thoi gian da duoc dinh dang la :", localtime1)


print(oct(73))
