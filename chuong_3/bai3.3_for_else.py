# Ví dụ cơ bản: for...else (không có break)
# for i in range(1, 4):
#     print("Lần lặp:", i)
# else:
#     print("Vòng lặp kết thúc bình thường!")

# Tìm số chia hết cho 7 trong dãy 10 → 13
# for i in range(10, 14):
#     print(f"Kiểm tra {i}...")
#     if i % 7 == 0:
#         print(f"Tìm thấy: {i} chia hết cho 7!")
#         break
# else:
#     print("Không có số nào chia hết cho 7")

# → Hết dãy, KHÔNG có break → else CHẠY


# Tìm số chia hết cho 7 trong dãy 10 → 20
for i in range(10, 21):
    print(f"Kiểm tra {i}...")
    if i % 7 == 0:
        print(f"Tìm thấy: {i} chia hết cho 7!")
        break
else:
    print("Không có số nào chia hết cho 7")

# → 14 % 7 == 0 → BREAK! → else KHÔNG CHẠY


