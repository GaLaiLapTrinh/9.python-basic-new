pw = input("Mời nhập vào mật khẩu: ")

#1 kiểm tra mk ít nhất 6 ký tự
has_length = len(pw) >= 6

#2 có ít nhất 1 chữ cái
# has_letter = False
# for c in pw:
#     if c.isalpha():
#         has_letter = True
#         break


#3 có ít nhất 1 chữ số
# has_digit = False
# for c in pw:
#     if c.isdigit():
#         has_digit = True
#         break
has_letter = any(c.isalpha() for c in pw)
has_digit = any(c.isdigit() for c in pw)

if has_length and has_letter and has_digit:
    print("Mật khẩu hợp lệ! ")
else:
    print("Mật khẩu 0 hợp lệ!")
    if not has_length:
        print("Cần có ít nhất 6 ký tự ")
    if not has_letter:
        print("Cần có ít nhất 1 chữ cái ")
    if not has_digit:
        print("Cần có ít nhất 1 số ")


