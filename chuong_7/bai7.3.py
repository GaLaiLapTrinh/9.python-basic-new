import random

print(random.randint(1,2))

#float
print(random.random()) #[0, 1)
print(random.uniform(1.1,1.2))  #[1.1, 1.2]

#xáo trộn
m = ["A", "B", 1,2,3,4,5]
random.shuffle(m)

print(m)


