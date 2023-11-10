def tinh_tien_dien(so_kwh):
    # Giá tiền điện theo bậc thang
    gia_bac_1 = 1678  # Giá bậc 1: từ 0 - 50 kWh
    gia_bac_2 = 1734  # Giá bậc 2: từ 51 -100 kWh
    gia_bac_3 = 2014  # Giá bậc 3: từ101 -200 kWh
    gia_bac_4 = 2536   # Giá bậc >200kWh

    if so_kwh <=50:
        tien_dien = so_kwh * gia_bac_1
    elif so_kwh <=100:
        tien_dien = (50 * gia_bac_1) + ((so_kwh-50) *gia_bac_2)
    elif so_kwh <=200:
        tien_dien =(50*gia_bac_1)+(50*gia_bac_2)+((so_kwh-100)*gia_bac_3)
        
    else:
        tien_dien =(50*gia_bac_1)+(50*gia_bac_2)+(100*gia_bac_3)+((so_kwh-200)*(gia_bac_4))

    return round(tien_dien,2)

# Nhập số lượng kWh sử dụng
so_kwh = float(input("Nhập số lượng kWh sử dụng: "))

# Tính tiền điện
tien_dien = tinh_tien_dien(so_kwh)

# In kết quả
print("Tiền điện cần thanh toán là:", tien_dien, "VNĐ")