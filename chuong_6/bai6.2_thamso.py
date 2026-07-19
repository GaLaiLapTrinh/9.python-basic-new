def gioi_thieu(ten, tuoi):
    print(ten, tuoi)

gioi_thieu("Nam", 27)

def tong(a, b=10):
    print(a, b)

tong(3, 15)

def tong_nhieu_gia_tri(a, b=10, c = 20):
    print(a, b, c)
tong_nhieu_gia_tri(3, c = 15)

def tinh_tong(a, b, *phan_con_lai):
    print("a= ", a)
    print("b= ", b)
    print("phần còn lại", phan_con_lai)

    tong = a+b
    for x in phan_con_lai:
        tong+=x

    return tong

kq = tinh_tong(4,5, 10, 11, 12, 13, 14)
print(kq)

def hien_thi_thong_tin(**thong_tin):
    print("Thông tin nhân viên")
    for k, v in thong_tin.items():
        print(k, v)

hien_thi_thong_tin(ten ="Nam", tuoi=27, que_quan = "Hà Nam")
hien_thi_thong_tin(ten ="Linh", tuoi=20, que_quan = "Hà Nội", cccd = "12345")


def cong(a,b,c):
    return a+b+c

cong_2 = lambda a,b,c: a+b+c

print(cong_2(10,20,30))