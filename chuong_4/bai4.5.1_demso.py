so = int(input("Mời nhập vào số từ 0 đến 99: "))
co_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

chuc = so // 10
dv = so % 10

if so < 10:
    # đọc theo mảng cơ sở
    kq = co_so[so]
elif so == 10:
    kq = "mười"
elif chuc ==1:
    if dv == 5:
        kq = "mười lăm"
    else:
        kq = "mười " + co_so[dv]
else:
    kq = co_so[chuc] + " mươi"
    if dv == 1:
        kq += " mốt"
    elif dv == 4:
        kq += " tư"
    elif dv == 5:
        kq += " lăm"
    elif dv != 0:
    kq+= " " + co_so[dv]

print(f"{so} → {kq}")