d = {
    "một" : 1,
    "hai" : 2,
    "ba" : 3
}

print(d)
print(type(d))

#cách 2
car = dict(
    brand = "Honda",
    model = "4",
    year = 2020,
)

print(car)
print(type(car))

# dict lồng nhau
school = {
    "office" : {'room1': "Tài chính", 'room2' : "Ngân hàng"} ,
    "lab" : {'lab1 ' : "Vật Lý", 'lap2' : "Hoá Học"}
}

#Truy cập giá trị
bike = {
    "name" : "Honda",
    "price" : 100,
    "year" : 2020
}

print(bike["name"])
# print(bike["name2"])

print("dùng .get an toàn hơn")
print(bike.get("name"))
print(bike.get("name2", "N/A"))

#thêm , sửa , xoá
d2 = {
    "name" : "Honda",
    "price" : 100,
}

d2["year"] = 2020
print(d2)

d2["price"] = 1000
print(d2)

del d2["year"]
print(d2)

#Dictionary — Duyệt key, value, items
d3 = {
    "name" : "Honda",
    "price" : 100,
    "year" : 2020,
}

print("duyệt for")
# duyệt key
for key in d3:
    print(key, ":", d3[key])

# Duyệt key + value (khuyên dùng)
print(d3.items())

for key, value in d3.items():
    print(key, ":", value)

#chỉ duyệt value
for value in d3.values():
    print(value)


#update
car2 = {
    "brand" : "Honda",
    "model" : "4",
    "year" : 2020
}

car3={
    "brand" : "Yamaha",
    "Color" : "Black"
}
car.update(car3)
print(car)

# ━━ .pop(key) — Xóa key, trả về value đã xóa
remove_car = car.pop("brand")
print(car)
print(remove_car)

# ━━ .popitem() — Xóa cặp cuối cùng
last = car.popitem()
print(car)
print(last)

# ━━ .setdefault(key, val) — Lấy value; chưa có → tự thêm
print(car)
car.setdefault("brand", "Yamaha")
print(car)
car.setdefault("model", "888888888888")
print(car)

# ━━ in — Kiểm tra tồn tại
print("brand22222" in car)

keys = {'a', 'e', 'i', 'o', 'u'}
d1 = dict.fromkeys(keys)
print(type(keys))

# ví dụ điểm danh
students = ["An", "Bình", "Cường", "Dũng"]
diem_danh = dict.fromkeys(students, False)
print(diem_danh)

diem_danh["An"] = True
print(diem_danh)
