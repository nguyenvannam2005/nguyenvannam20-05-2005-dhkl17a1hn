# cách nhận biết 1 năm nhuận và 1 năm không nhuận 
a = int(input("nhập năm:"))
if (a % 400 == 0) or ((a % 4 == 0) and (a % 100!=0)):
     b = "năm nhuận"
     a = "năm không nhuận"
     print("năm đó là năm nhuận", b)
else:
     print("năm đó không phải năm nhuận", a)