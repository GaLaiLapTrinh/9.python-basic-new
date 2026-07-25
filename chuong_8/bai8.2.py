import os
#current working directory
print(os.getcwd())

# Liệt kê tất cả file và thư mục trong thư mục hiện tại
print(os.listdir("."))
# ".." = thư mục cha (lùi lên 1 cấp)
print(os.listdir(".."))
# Liệt kê thư mục bất kỳ qua đường dẫn tuyệt đối
print(os.listdir("C:\\Users\\tuhoc.cc\\Desktop\\duan_py\\chuong_6"))

# tạo
# os.mkdir("test")
# tạo thư mục nhiều cấp nếu chưa có
# os.makedirs("data/2026/logs")
# os.makedirs("data/2026/bug")
# xoá
# os.rmdir("test")

#đổi tên
# os.rename("xx.txt", "t2.txt")

#xoá
# os.remove("abc.txt")

kt = os.path.exists("abc.txt")
if kt:
    os.remove("abc.txt")
else:
    print("không tồn tại tệp abc.txt")


thumuc_hien_tai = os.getcwd()
print(thumuc_hien_tai)
new_path = os.path.join(thumuc_hien_tai, "t.txt")
print(new_path)

print(os.path.basename(new_path))
print(os.path.dirname(new_path))

print(os.path.getsize(new_path))
ten_file = os.path.basename(new_path)
tach = os.path.splitext(ten_file)
print(tach)
print(tach[0])

#os walk
# path_root = "C:\\Users\\tuhoc.cc\\Desktop\\duan_py"
# for dirpath, dirnames, filenames in os.walk(path_root):
#     print(dirpath)
#     print(f"thư mục con{dirnames}")
#     print( f"các tệp con {filenames}")
#     print("kết thúc 1 lượt ")

print("###################################")
new_path_2 = "C:\\Users\\tuhoc.cc\\Desktop\\duan_py\\chuong_7"
for dirpath, dirnames, filenames in os.walk(new_path_2):
    for filename in filenames:
        if filename.endswith(".txt"):
            print(dirpath)
            print(filename)
            duong_dan_file = os.path.join(dirpath, filename)
            print(duong_dan_file)






