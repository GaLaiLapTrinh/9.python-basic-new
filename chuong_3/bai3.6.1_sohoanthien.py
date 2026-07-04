# so = int(input("Mời nhập vào 1 số: "))
#
# tong_uoc = 0
# for i in range(1, so):
#     if so % i == 0:
#         tong_uoc += i
#
# if so == tong_uoc:
#     print(f"{so} là số hoàn hảo")
# else:
#     print(f"{so} không phải số hoàn hảo")

print("Các số hoàn thiện từ 1-1000:")
for n in range(2, 1001):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    if tong_uoc == n:
        print(n, end=' ')

