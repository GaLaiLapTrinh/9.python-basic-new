csdl = {
    "2026001": {"ten": "Nguyễn Văn A", "bo_phan": "CNC"},
    "2026002": {"ten": "Trần Thị B",   "bo_phan": "QA"},
}
print(csdl.items())
t = (4, 5)
a, b = t

while True:
    print("\n ======= QUẢN LÝ NHÂN SỰ =======")
    print("1. Hiển thị")
    print("2. Thêm")
    print("3. Sửa")
    print("4. Xoá")
    print("5. Thoát")
    chon = input("Mời nhập vào lựa chọn(1-5): ").strip()

    # ------1. Hiển Thị ---------
    if chon == "1":
        if len(csdl) == 0:
            print("CSDL trống")
        else:
            print(f"{'Mã Gen' :<10} {'Họ và Tên' :<20} {'Bộ phận'}")
            print("-"*40)
            for gen, info in csdl.items():
                print(f"{gen:<10} {info["ten"]:<20} {info["bo_phan"]}")

    # ------2. Thêm ---------
    elif chon == "2":
        gen = input("Nhập mã gen: ").strip()
        while not gen:
            print("🙏 Không được để trống, nhập lại")
            gen = input("Nhập mã gen: ").strip()
        if gen in csdl:
            print(f"🙏 Mã gen {gen} đã tồn tại, kiểm tra lại")
        else:
            ten = input("Nhập tên: ").strip()
            while not ten:
                print("🙏 Không được để trống, nhập lại")
                ten = input("Nhập tên: ").strip()

            bp = input("Nhập bộ phận: ").strip()
            while not bp:
                print("🙏 Không được để trống, nhập lại")
                bp = input("Nhập bộ phận: ").strip()

            csdl[gen] = {"ten": ten, "bo_phan": bp}
            print(f"🩳 Đã thêm nhân sự {gen}")


    # ━━ 3. SỬA ━━
    elif chon == "3":
        gen = input("Nhập mã GEN cần sửa: ").strip()
        while not gen:
            print("❌ Không được để trống, nhập lại!")
            gen = input("Nhập mã GEN cần sửa: ").strip()
        if gen not in csdl:
            print(f"❌ Mã GEN '{gen}' không tồn tại!")
        else:
            print(f"Thông tin hiện tại: {csdl[gen]}")
            ten = input("Nhập Họ và Tên mới: ").strip()
            while not ten:
                print("❌ Không được để trống, nhập lại!")
                ten = input("Nhập Họ và Tên mới: ").strip()
            bp = input("Nhập Bộ Phận mới: ").strip()
            while not bp:
                print("❌ Không được để trống, nhập lại!")
                bp = input("Nhập Bộ Phận mới: ").strip()
            csdl[gen] = {"ten": ten, "bo_phan": bp}
            print(f"✅ Đã sửa nhân sự '{gen}'")

    # ━━ 4. XÓA ━━
    elif chon == "4":
        gen = input("Nhập mã GEN cần xóa: ").strip()
        while not gen:
            print("❌ Không được để trống, nhập lại!")
            gen = input("Nhập mã GEN cần xóa: ").strip()
        if gen not in csdl:
            print(f"❌ Mã GEN '{gen}' không tồn tại!")
        else:
            del csdl[gen]
            print(f"✅ Đã xóa nhân sự '{gen}'")

    # ━━ 5. THOÁT ━━
    elif chon == "5":
        print("Tạm biệt!")
        break

    else:
        print("⚠️ Lựa chọn không hợp lệ, vui lòng chọn 1-5")


