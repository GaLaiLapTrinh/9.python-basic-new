tong = 0

for n in range(2, 100):
    la_nguyen_to = True
    for i in range(2, n):
        if n % i == 0:
            la_nguyen_to = False
            break
    if la_nguyen_to:
        print(n, end=" ")
        tong += n

print()
print("Tổng các số nguyên tố:", tong)
