import time

print(time.time())

t = time.localtime()
print(t)
print(t.tm_year)
print(t.tm_mon, t.tm_mday)

print(time.asctime(t))

# for i in range(5):
#     print(i)
#     time.sleep(2.8)

bat_dau = time.time()
tong = 0
for i in range(1_000_000):
    tong += i
ket_thuc = time.time()
print(f"thời gian chạy code: {ket_thuc-bat_dau:.4f} giây")
