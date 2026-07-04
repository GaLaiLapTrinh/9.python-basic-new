import random

n = int(input("Mời nhập vào số phần tử của list: "))

lst = []
for i in range(n):
    lst.append(random.randint(1, 100))

print("List random vừa tạo là: ", lst)