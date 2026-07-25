# f = open("a.txt","w")
# print("Sau bước tạo đối tượng file")
# f.write("Hello")
# print("Sau bước f.write")
# f.close()
# print("Sau bước close")

# r +
# f = open("t.txt","r+")
# f.write("XY")
# f.seek(0)
# print(f.read())
# f.close()

#w+
# f = open("t.txt","w+")
# print(f.read())
# f.write("XY")
# #di chuyển con trỏ về đầu file
# f.seek(0)
# print(f.read())
# f.close()

#a+
# f = open("t.txt","a+")
# print(f.read())
# f.seek(0)
# print(f.read())
# f.write("234234234")
# f.close()

# f = open("t.txt")
# noi_dung = f.read()
# print(noi_dung)
# print(type(noi_dung))

# f = open("t.txt")
# ds_lines = f.readlines()
# print(ds_lines)
# for line in ds_lines:
#     print(line.strip())
# f.close()
#
# f2 = open("t2.txt", "w", encoding="utf-8")
# f2.writelines(ds_lines)
# f2.close()

with open("diem.txt","r",encoding="utf-8") as f:
    for line in f:
        ten, diem = line.strip().split(",")
        print(f"{ten} - {diem}")










