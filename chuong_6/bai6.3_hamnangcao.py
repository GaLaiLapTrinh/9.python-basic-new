def giai_thua(n):
    if n <=1:
        return 1
    return n * giai_thua(n-1)

kq = giai_thua(4)
print(kq)