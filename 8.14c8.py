# Yêu cầu người dùng nhập số nguyên N
N = int(input("Nhập số nguyên N: "))
# Khởi tạo biến tổng S
S = 0
# Duyệt qua N lần để nhập từng số nguyên
for i in range(N):
    num = int(input(f"Nhập số nguyên thứ {i+1}: "))
    S += num
# In ra tổng S
print(f"Tổng {N} số nguyên bạn đã nhập là: {S}")
# Yêu cầu người dùng nhập số nguyên N
N = int(input("Nhập số nguyên N: "))
# Đọc danh sách số nguyên từ người dùng
numbers = []
for i in range(N):
    num = int(input(f"Nhập số nguyên thứ {i+1}: "))
    numbers.append(num)
# Tính tổng của danh sách số nguyên
S = sum(numbers)
# In ra tổng S
print(f"Tổng {N} số nguyên bạn đã nhập là: {S}")