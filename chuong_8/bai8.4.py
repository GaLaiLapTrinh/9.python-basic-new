from calendar import month
from datetime import datetime, timedelta

hien_tai = datetime.now()
print(hien_tai)

print(hien_tai.year)
print(hien_tai.month)
print(hien_tai.day)
print(hien_tai.hour)
print(hien_tai.minute)
print(hien_tai.second)

d1 = datetime(2018,12,10,14,15,10)
print(d1)

now = datetime.now()
print(now)
sang = datetime(now.year,now.month,now.day, 8)
chieu = datetime(now.year,now.month,now.day, 16)

if sang <= now <= chieu:
    print("Giờ làm việc")
else:
    print("Giờ nghỉ ngơi")

#time delta
# cộng thêm 7  ngày nữa
tuan_sau = now + timedelta(days=8, hours=10)
print(tuan_sau)

# tính thử sinh nhật còn bao nhiêu ngày
sinh_nhat = datetime(2026,9, 15)
con_lai = (sinh_nhat - now)
print(con_lai)

# datetime =>  chuỗi
print(now.strftime("%A, %d/%m/%Y %H:%M:%S"))

# ép chuỗi sang kiểu date time
s = "25/12/2025 09:00"
d = datetime.strptime(s, "%d/%m/%Y %H:%M")
print(d)
print(type(d))