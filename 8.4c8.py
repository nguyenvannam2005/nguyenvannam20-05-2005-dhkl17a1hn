from math import sqrt
a = int(input("nhập giá trị a:"))
b = int(input("nhập giá trị b:"))
c = int(input("nhập giá trị c:"))
p = (a+b+c)/2
print('Diện tích:',sqrt(p*(p-a)*(p-b)*(p-c)))
print('chu vi', p)