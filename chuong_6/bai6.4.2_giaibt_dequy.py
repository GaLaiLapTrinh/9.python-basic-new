def tong_de_quy(n):
    if n <=1:
        return 1
    return n + tong_de_quy(n-1)

print(tong_de_quy(3))