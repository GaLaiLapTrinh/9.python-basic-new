year = int(input("Nhập năm: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} là năm nhuận")
else:
    print(f"{year} không phải năm nhuận")

# Tìm tất cả năm nhuận 2000-2100
print("Năm nhuận từ 2000-2100:")
for y in range(2000, 2101):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print(y, end=' ')
