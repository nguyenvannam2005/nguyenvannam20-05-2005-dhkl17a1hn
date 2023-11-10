m = int(9)
n = int(900)
if n <= m:
    print("vui lòng nhập số sao cho m lớn hơn n")
else:
    print(f"Các số chia hết cho {m} trong khoảng từ 1 đến {n} là:")
    for x in range(1, n + 1):
        if x % m == 0:
            print(x)