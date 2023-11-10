def tinh_cuoc_taxi(loai_xe, so_km, thoi_gian_cho):
    if loai_xe == 4:
        gia_mo_cua = 11000
        gia_dau_km = 12100
        gia_tiep_theo = 10000
    elif loai_xe == 7:
        gia_mo_cua = 13000
        gia_dau_km = 14100
        gia_tiep_theo = 12000
    else:
        return "Loại xe không hợp lệ. Vui lòng nhập lại."

    cuoc_taxi = gia_mo_cua + (so_km - 0.8) * (gia_dau_km if so_km <= 20 else gia_tiep_theo)
    cuoc_taxi = gia_mo_cua + (so_km - 0.8) * (gia_dau_km if so_km <= 30 else gia_tiep_theo)
    tien_cho = max(0, thoi_gian_cho - 5) * 800

    tong_tien = cuoc_taxi + tien_cho

    return tong_tien

loai_xe1, so_km1, thoi_gian_cho1 = (4, 10, 3)
loai_xe2, so_km2, thoi_gian_cho2 = (7,30 ,10)

tong_tien1= tinh_cuoc_taxi(loai_xe1 ,so_km1 ,thoi_gian_cho1 )
tong_tien2= tinh_cuoc_taxi(loai_xe2 ,so_km2 ,thoi_gian_cho2 )

print("Tổng tiền chuyến đi xe 4 chỗ:", tong_tien1)
print("Tổng tiền chuyến đi xe 7 chỗ:", tong_tien2)