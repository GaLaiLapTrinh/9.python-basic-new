from tien_ich import nhap_khong_rong

csdl = {
    "2026001": {"ten": "Nguyễn Văn A", "bo_phan": "CNC"},
    "2026002": {"ten": "Trần Thị B",   "bo_phan": "QA"},
}

def hien_thi():
    if len(csdl) == 0:
        print("CSDL trống")
    else:
        print(f"{'Mã Gen' :<10} {'Họ và Tên' :<20} {'Bộ phận'}")
        print("-" * 40)
        for gen, info in csdl.items():
            print(f"{gen:<10} {info["ten"]:<20} {info["bo_phan"]}")

def them():
    gen = nhap_khong_rong("Nhập mã gen: ")
    if gen in csdl:
        print(f"🙏 Mã gen {gen} đã tồn tại, kiểm tra lại")
    else:
        ten = nhap_khong_rong("Nhập tên: ")
        bp= nhap_khong_rong("Nhập bộ phận: ")
        csdl[gen] = {"ten": ten, "bo_phan": bp}
        print(f"🩳 Đã thêm nhân sự {gen}")

def sua():
    gen = nhap_khong_rong("Nhập mã gen: ")
    if gen not in csdl:
        print(f"❌ Mã GEN '{gen}' không tồn tại!")
    else:
        print(f"Thông tin hiện tại: {csdl[gen]}")
        ten = nhap_khong_rong("Nhập tên: ")
        bp = nhap_khong_rong("Nhập bộ phận: ")
        csdl[gen] = {"ten": ten, "bo_phan": bp}
        print(f"✅ Đã sửa nhân sự '{gen}'")

def xoa():
    gen = nhap_khong_rong("Nhập mã gen: ")
    if gen not in csdl:
        print(f"❌ Mã GEN '{gen}' không tồn tại!")
    else:
        del csdl[gen]
        print(f"✅ Đã xóa nhân sự '{gen}'")