n = int(input("Nhập vào số phần tử của mảng: "))
lst = []
for i in range(n):
    x = int(input(f"Mời nhập vào phần tử thứ {i+1}: "))
    lst.append(x)

print("Danh sách bạn vừa nhập là: ", lst)

# tách thành 2 list chẵn lẻ
chan =[]
le = []
for x in lst:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)

print("Chẵn : ", chan)
print("Lẻ: ", le)