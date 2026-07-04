# list
x = [1, 3, "Hello", [1,5,7,8], True, False]

numbers = [10, 2, 3, 4, 55]
rong = []

print(numbers[0])
print(numbers[-1])
print(numbers[4])

s = ["a", "b", "c", "d", "e"]

print(s[2:4])
print(s[::-1])
print("mảng hiện tại")
print(s)
print("mảng sau khi thay đổi phần tử index 0")
s[0] = "xxxxx"
print(s)

#duyệt for
for i in numbers:
    if i == 55:
        print("Có giá trị 55 ở trong mảng")

# xoá
numbers_2 = [1, 2, 3, 4, 5]
del numbers_2[:2]
print(numbers_2)

#xoá theo giá trị
numbers_3 = [1, 2, 3, 4, 5]
numbers_3.remove(2)
print(numbers_3)

# sắp xếp
numbers_4 = [9, 2, 8, 4, 5]
numbers_4.sort()
print(numbers_4)

chuoi = ["z", "x", "c", "d", "e"]
chuoi.sort()
print(chuoi)

chuoi.reverse()
print(chuoi)

# xoá pop
numbers_5 = [1, 2, 3, 4, 5]
gia_tri = numbers_5.pop(1)
print(numbers_5)
print(gia_tri)

# xoá remove
numbers_6 = [1, 2, 3, 4, 5, 1, 1, 1, 1]
numbers_6.remove(1)
print(numbers_6)

numbers_6.clear()
print(numbers_6)

# khác
numbers_7 = [99,1, 2, 3, 4, 5, 1, 1, 100,-5]
print(len(numbers_7))
print(max(numbers_7))
print(min(numbers_7))
print(numbers_7.count(1))

#.index tìm vị trí, trả về vị trí index đầu tiên xuất hiện trong list, nếu 0 tìm thấy báo lỗi
print(numbers_7.index(1))


print("+++++++++++++++++++++++++===================++++++++++")
numbers_8 = [1, 2, 3, 4, 5]
numbers_9 = numbers_8.copy()
print(numbers_8)
print(numbers_9)

numbers_9.clear()
print(numbers_8)
print(numbers_9)