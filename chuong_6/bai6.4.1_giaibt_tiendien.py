def tinh_tien_dien(so_kwh):
    """Tính tiền điện theo bậc thang EVN. Trả về số tiền (đồng)."""
    if so_kwh <= 50:
        return so_kwh * 1678
    elif so_kwh <= 100:
        return 50*1678 + (so_kwh - 50) * 1734
    elif so_kwh <= 200:
        return 50*1678 + 50*1734 + (so_kwh - 100) * 2014
    else:
        return 50*1678 + 50*1734 + 100*2014 + (so_kwh - 200) * 2536

kwh = int(input("Nhập số kWh tiêu thụ: "))
tien = tinh_tien_dien(kwh)
print(f"Số điện: {kwh} kWh / Tiền điện: {tien:,} đồng")

