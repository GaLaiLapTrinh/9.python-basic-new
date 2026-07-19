list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly" , "dd", "ddd"]

kq = []

# for i in range(len(list1)):
#     kq.append(list1[i]+list2[i])
#
# print(kq)

print(list(zip(list1, list2)))

kq2 = []
for a, b in zip(list1, list2):
    kq2.append(a + b)
print(kq2)