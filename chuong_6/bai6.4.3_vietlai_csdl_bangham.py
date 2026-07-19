csdl = {
    "2026001": {"ten": "Nguyễn Văn A", "bo_phan": "CNC"},
    "2026002": {"ten": "Trần Thị B",   "bo_phan": "QA"},
}

def hien_thi(csdl):
    if len(csdl) == 0:
        print("CSDL trống")
    else:
        print(f"{'Mã Gen' :<10} {'Họ và Tên' :<20} {'Bộ phận'}")
        print("-" * 40)
        for gen, info in csdl.items():
            print(f"{gen:<10} {info["ten"]:<20} {info["bo_phan"]}")


def nhap_khong_rong(thong_bao):
    gia_tri = input(thong_bao).strip()
    while not gia_tri:
        print("🙏 Không được để trống, nhập lại")
        gia_tri = input(thong_bao).strip()
    return gia_tri


def them(csdl):
    gen = nhap_khong_rong("Nhập mã gen: ")
    if gen in csdl:
        print(f"🙏 Mã gen {gen} đã tồn tại, kiểm tra lại")
    else:
        ten = nhap_khong_rong("Nhập tên: ")
        bp= nhap_khong_rong("Nhập bộ phận: ")
        csdl[gen] = {"ten": ten, "bo_phan": bp}
        print(f"🩳 Đã thêm nhân sự {gen}")

def sua(csdl):
    gen = nhap_khong_rong("Nhập mã gen: ")
    if gen not in csdl:
        print(f"❌ Mã GEN '{gen}' không tồn tại!")
    else:
        print(f"Thông tin hiện tại: {csdl[gen]}")
        ten = nhap_khong_rong("Nhập tên: ")
        bp = nhap_khong_rong("Nhập bộ phận: ")
        csdl[gen] = {"ten": ten, "bo_phan": bp}
        print(f"✅ Đã sửa nhân sự '{gen}'")

def xoa(csdl):
    gen = nhap_khong_rong("Nhập mã gen: ")
    if gen not in csdl:
        print(f"❌ Mã GEN '{gen}' không tồn tại!")
    else:
        del csdl[gen]
        print(f"✅ Đã xóa nhân sự '{gen}'")

while True:
    print("\n ======= QUẢN LÝ NHÂN SỰ =======")
    print("1. Hiển thị")
    print("2. Thêm")
    print("3. Sửa")
    print("4. Xoá")
    print("5. Thoát")
    chon = input("Mời nhập vào lựa chọn(1-5): ").strip()

    # ------1. Hiển Thị ---------
    if chon == "1":  hien_thi(csdl)
    # ------2. Thêm ---------
    elif chon == "2": them(csdl)

    # ━━ 3. SỬA ━━
    elif chon == "3":
        sua(csdl)

    # ━━ 4. XÓA ━━
    elif chon == "4":
        xoa(csdl)

    # ━━ 5. THOÁT ━━
    elif chon == "5":
        print("Tạm biệt!")
        break

    else:
        print("⚠️ Lựa chọn không hợp lệ, vui lòng chọn 1-5")


