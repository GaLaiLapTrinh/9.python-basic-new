from collections import Counter

text = "Trong năm 2018 và nửa đầu năm 2019, số dự án từ Trung Quốc đăng ký đầu tư vào Việt Nam tăng mạnh nhưng với quy mô khá nhỏ (91% dự án dưới 10 triệu USD)"

words = text.lower().split()
print(words)

freq = Counter(words)
print(freq)

print("Top 5 từ xuất hiện nhiều nhất: ")
print(freq.most_common(5))
for word, count in freq.most_common(5):
    print(f"{word}: {count} lần")