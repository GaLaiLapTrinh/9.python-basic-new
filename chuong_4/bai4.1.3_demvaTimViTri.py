n = int(input("Mời nhập vào số lượng phần tử list: "))
lst = []
for i in range(n):
    x = int(input(f"Mời nhập vào phần tử thứ {i+1}: "))
    lst.append(x)

print("List bạn vừa nhập là: ", lst)

# Đếm và lưu vị trí
dem = 0
vi_tri =[]
for i in range(n):
    if lst[i] < 5:
        dem += 1
        vi_tri.append(i)

print(f"Có {dem} số nhỏ hơn 5 ở trong lst")
print("Vị trí index các số nhỏ hơn 5 là: ", vi_tri)
