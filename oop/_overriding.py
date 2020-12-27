"""
Ghi đè phương thức trong Python
"""
class Bank:
    def getRoi(self):
        return 10

class ACB(Bank):
    def getRoi(self):
        return 7

class BIDV(Bank):
    def getRoi(self):
        return 8

b1 = Bank()
b2 = ACB()
b3 = BIDV()
print("Lãi suất tiết kiệm:", b1.getRoi())
print("Lãi suất tiết kiệm cua ACB:", b2.getRoi())
print("Lãi suất tiết kiệm cua BIDV:", b3.getRoi())