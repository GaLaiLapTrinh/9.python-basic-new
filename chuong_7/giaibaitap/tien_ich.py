def nhap_khong_rong(thong_bao):
    gia_tri = input(thong_bao).strip()
    while not gia_tri:
        print("🙏 Không được để trống, nhập lại")
        gia_tri = input(thong_bao).strip()
    return gia_tri