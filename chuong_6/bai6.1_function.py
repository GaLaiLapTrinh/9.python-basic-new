def tinh_tong(a,b):
    tong = a +b
    print(f"{a} + {b} = {tong}")



tinh_tong(5,3)
tinh_tong(51,12)
tinh_tong(7,3)

def chao_buoi_sang():
    print("Chào buổi sáng")
    print("Chúc một ngày tốt lành")

chao_buoi_sang()

def chao_ten(xyz):
    print(f"Xin chào {xyz}")
    print(f"Rất vui được gặp bạn")

chao_ten("An")
chao_ten("Bình")

def lay_ty_gia():
    #logic đi lấy tỷ giá ở trên mạng,
    return 26000

ty_gia = lay_ty_gia()
print(ty_gia)

def dt_hv(canh):
    dt = canh * canh
    return dt

kq1 = dt_hv(10)

def tinh_toan(a,b):
    return a+b, a*b

kq = tinh_toan(10,20)
print(kq)
print(type(kq))

so_a, so_b = kq
print(so_a)
print(so_b)


def kiem_tra_am(so):
    if so < 0:
        return "Âm"
    if so == 0:
        return "Không"
    return "Dương"

kiem = kiem_tra_am(0)

def tinh_gia(don_gia, so_luong):
    tong_tien = so_luong * don_gia
    return tong_tien

THUE_VAT = 0.1

def tinh_gia_sau_thue(gia_goc):
    global THUE_VAT
    THUE_VAT = 0.01
    return gia_goc * (1+ THUE_VAT)

print(tinh_gia_sau_thue(10))