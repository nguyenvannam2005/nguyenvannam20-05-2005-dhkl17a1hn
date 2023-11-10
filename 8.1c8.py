a = int(input("nhập hệ số a"))
b = int(input("nhập hệ số b"))
c = int(input("nhập hệ số c"))
d = int(input("nhập hệ số d"))
max_num = a
min_num = b
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c
if d > max_num:
    max_num = d
if b < min_num:
    min_num = b
if c < min_num:
    min_num = c
if d < min_num:
    min_num = d
print("in số lớn nhất", max_num)
print("in số bé nhất", min_num)

