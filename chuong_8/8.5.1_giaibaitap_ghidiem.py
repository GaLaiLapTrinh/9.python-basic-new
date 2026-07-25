# bước 1: ghi
with open("diem.txt", "w", encoding="utf-8") as f:
    for i in range(3):
        ten = input(f"Tên HS {i+1}: ")
        diem = input(f"Điểm HS {i+1}: ")
        f.write(f"{ten},{diem}\n")


# bước 2: đọc
with open("diem.txt", "r", encoding="utf-8") as f:
    for dong in f:
        print(dong.strip().split(","))
        ten, diem = dong.strip().split(",")
        print(f"{ten} : {diem}")
