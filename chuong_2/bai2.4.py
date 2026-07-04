tong_so_phut = 135
gio = tong_so_phut // 60
phut = tong_so_phut % 60
print(gio)
print(phut)
print(f"{gio} giờ {phut} phút")

#phép logic
a = 5
b = 5
c = 7

ket_qua = (a == b) or (a == c)
print(ket_qua)

# phép gán phức hợp
diem = 80
# diem = diem +5
diem-=5
print(diem)

# gán nhiều biến
x = y = z = 0
print(x)
print(y)
print(z)

#gán khác giá trị trên 1 dòng
a, b, c = 1, 2, 3

print(a, b, c)

#hoán đổi 2 biến, 0 cần biến tạm
a, b = b, a
print(a, b)
