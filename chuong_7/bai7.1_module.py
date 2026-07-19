# cách 1
# import phep_tinh
#
# kq = phep_tinh.cong(4,5)
# print(kq)

# cách 2:
# from phep_tinh import cong, nhan
#
# print(cong(4,5))
# print(nhan(4,5))

# lưu ý __name__
from phep_tinh import show_name
print(__name__)

show_name()
