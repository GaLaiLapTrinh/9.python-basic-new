s = "       Xin chào      "
print(s)
print(s.strip())

s2 = "    #xin chào##!###   "
print(s2)
print(s2.strip(" #"))

s3 = "ab54654545ab65454ab55"
s4 = s3.replace("ab", "XX", 2)
print(s4)

s5 = "học python rất là dễ"
print(s5.split("y"))

# bài tập 5.5
dong = "An,25,HN"
# phan_tach = dong.split(",")
# print(phan_tach)
# ten = phan_tach[0]
# tuoi = phan_tach[1]
# tp = phan_tach[2]

ten, tuoi, tp = dong.split(",")
print(ten, tuoi, tp)

s6 = "abcdefghijklmnopppppppp"
print(s6.find("9"))


s7 = "aaaa sss"
print(s7.isalnum())
print(s7.capitalize())

# giải bài tập 5.7
files = ["baocao.pdf", "nganngo.txt", "ghichu.txt", "anhdep.png"]
for file in files:
    if file.endswith(".txt"):
        print(file)

# kiểm tra mã đúng
ma_dung = ["6B", "7C", "AB"]
nhap_ma = input("Mời nhập vào mã: ")
if nhap_ma in ma_dung:
    print("hợp lệ")
else:
    print("không hợp lệ ")

