import re
s = "English = 78 Science = 83 Math = 68 History = 65"

numbers_str = re.findall(r"\d+", s)
print(numbers_str)

# chuyển từng phần tử của mảng numbers_str sang số
# numbers = []
# for num in numbers_str:
#     numbers.append(int(num))

numbers = [int(n) for n in numbers_str]
print(numbers)
# tính toán
print("Tổng", sum(numbers))
print("TB", sum(numbers) / len(numbers))