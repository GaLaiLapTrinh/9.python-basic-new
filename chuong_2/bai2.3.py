from fractions import Fraction

a = 42
b = -7
c = 0
print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# số thực
d = 3.14
e = -0.5

print(d)
print(e)

print(type(d))
print(type(e))

#fraction
f = Fraction('0.25')
print(f)
print(type(f))

# Falsy value
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(None))

#truthy value
print(bool(1321))
print(bool("sdfsdf"))

print(float(120))

# ép kiểu
my_number = 105.9
so_nguyen = int(my_number)
print(so_nguyen)
