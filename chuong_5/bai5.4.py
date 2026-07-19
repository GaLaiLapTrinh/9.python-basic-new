from collections import Counter

chuoi = "toi rat thich hoc python"

# đếm
freq = Counter(chuoi)
print(freq)


print(freq['t'])
print(freq['ab'])

print(freq.most_common(3))
for k, v in freq.most_common(3):
    print(k, v)


numbers_str = ['78', '83', '68', '65']
# Cách 1: for thông thường (dễ đọc)
numbers = []
for n in numbers_str:
    numbers.append(int(n))
print(numbers)


