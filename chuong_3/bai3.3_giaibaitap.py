# n = int(input("mời nhập vào n nguyên dương: "))
# gt = 1
# for i in range(1, n + 1):
#     gt = gt * i
# print(gt)
# 5! = 5*4*3*2*1 = 1*2*3*4*5

tong = 0
for i in range(1, 11):
    gt = 1
    for j in range(1, i + 1):
        gt *= j # gt = gt * j
    tong += gt # tong = tong + gt
print("Tổng 1! + 2! + ... + 10! =", tong)
