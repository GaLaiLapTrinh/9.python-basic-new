import os

FILE = "csdl.txt"

# hàm tiện ích giữ nguyên
def hien_thi(csdl):
    if len(csdl) == 0:
        print("CSDL trống")
    else:
        print(f"{'Mã Gen' :<10} {'Họ và Tên' :<20} {'Bộ phận'}")
        print("-" * 40)
        for gen, info in csdl.items():
            print(f"{gen:<10} {info['ten']:<20} {info['bo_phan']}")


def nhap_khong_rong(thong_bao):
    gia_tri = input(thong_bao).strip()
    while not gia_tri:
        print("🙏 Không được để trống, nhập lại")
        gia_tri = input(thong_bao).strip()
    return gia_tri
# thêm hàm mới: đọc/ ghi file csdl.txt
def doc_csdl():
    if not os.path.exists(FILE):
        return {}
    csdl = {}
    with open(FILE, "r", encoding="utf-8") as f:
        for dong in f:
            dong = dong.strip()
            if not dong:
                continue
            gen,ten, bp = dong.split(",")
            csdl[gen] = {"ten": ten, "bo_phan": bp}
    return csdl

def ghi_csdl(csdl):
    with open(FILE, "w", encoding="utf-8") as f:
        for gen, info in csdl.items():
            f.write(f"{gen},{info['ten']},{info['bo_phan']}\n")


def them(csdl):
    gen = nhap_khong_rong("Nhập mã gen: ")
    if gen in csdl:
        print(f"🙏 Mã gen {gen} đã tồn tại, kiểm tra lại")
    else:
        ten = nhap_khong_rong("Nhập tên: ")
        bp= nhap_khong_rong("Nhập bộ phận: ")
        csdl[gen] = {"ten": ten, "bo_phan": bp}
        ghi_csdl(csdl)
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
        ghi_csdl(csdl)
        print(f"✅ Đã sửa nhân sự '{gen}'")

def xoa(csdl):
    gen = nhap_khong_rong("Nhập mã gen: ")
    if gen not in csdl:
        print(f"❌ Mã GEN '{gen}' không tồn tại!")
    else:
        del csdl[gen]
        ghi_csdl(csdl)
        print(f"✅ Đã xóa nhân sự '{gen}'")

#chương trình chính
csdl = doc_csdl()

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


