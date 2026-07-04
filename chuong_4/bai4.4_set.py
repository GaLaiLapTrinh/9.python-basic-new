s = {1, 1, 2, 2, 3, 4, 5}

print(s)
print(type(s))

# set rỗng
abc = {}
print(abc)
print(type(abc))

set_rong = set()
print(set_rong)
print(type(set_rong))

# thêm, xoá phần tử
print("2.Thêm xoá phần tử")
s2 = {1,2,3}
print(s2)
print(len(s2))

s2.add(100)
print(s2)

print("3. Thêm nhiều phần tử")
s2.update([101,202])
print(s2)

print("4. xoá bằng remove, nếu 0 tồn tại thì báo lỗi")
s2.remove(202)
print(s2)

print("5. xoá bằng discard, an toàn hơn")
s2.discard(203)
print(s2)

print("6. xoá tất cả")
s2.clear()
print(s2)


print("7. phép toán tập hợp")

A = {'C', 'D', 'E', 'F', 'G'}
B = {'E', 'F', 'G', 'A', 'B'}
print(A)
print(B)

print(A-B) # hiệu
print(A | B) # hợp
print(A & B) # giao
print(A ^ B)  # hiệu đối xứng

print("8. ứng dụng")
ten = ["An", "Bình", "Bình", "Linh", "Khang", "An"]
unique = list(set(ten))
print(unique)

print("9. tìm phần tử chung giữa 2 list")
list1 = [1,2,3,4,5]
list2 = [1,2,3,99,100]

comon = list(set(list1) & set(list2))
print(comon)
