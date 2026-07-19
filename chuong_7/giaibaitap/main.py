import quan_ly_ns as ql

while True:
    print("\n ======= QUẢN LÝ NHÂN SỰ =======")
    print("1. Hiển thị")
    print("2. Thêm")
    print("3. Sửa")
    print("4. Xoá")
    print("5. Thoát")
    chon = input("Mời nhập vào lựa chọn(1-5): ").strip()

    if chon == "1":  ql.hien_thi()
    elif chon == "2": ql.them()
    elif chon == "3":  ql.sua()
    elif chon == "4":   ql.xoa()
    elif chon == "5":
        print("Tạm biệt!")
        break
    else:
        print("⚠️ Lựa chọn không hợp lệ, vui lòng chọn 1-5")