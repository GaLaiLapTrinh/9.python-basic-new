n = int(input("Mời nhập vào số phần tử của list: "))

lst =[]
for i in range(n):
    x = int(input(f"Mời nhập vào phần tử thứ {i+1}: "))
    lst.append(x)

print("List bạn vừa nhập là: ", lst)

#1 bình phương từng phần tử và nhét vào list mới
binh_phuong =[]
for x in lst:
    binh_phuong.append(x**2)
print("List bình phương là: ", binh_phuong)

#2 đếm phần tử > 50 của danh sách lst
dem = 0
for x in lst:
    if x > 50:
        dem += 1 # dem = dem + 1
print("Số lượng phần tử >50 của lst là: ", dem)