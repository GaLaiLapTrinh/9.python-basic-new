from collections import Counter

chu = "abracadabra"
freq = Counter(chu)
print(freq.most_common(2))

print("In ra 2 ký tự xuất hiện nhiều nhất")
for ky_tu, count in freq.most_common(2):
    print(f"{ky_tu} xuất hiện {count} lần")