# ==========================================
# HOẠT ĐỘNG 6: MINI PROJECT 1 - QUẢN LÝ SINH VIÊN BẰNG LIST
# ==========================================
print("=== HOẠT ĐỘNG 6: QUẢN LÝ SINH VIÊN ===")

danh_sach_sv = [(8.5, "An"), (7.0, "Bình"), (9.2, "Chi"), (6.5, "Dung")]

# Them sinh vien moi
danh_sach_sv.append((8.0, "Em"))

# Xoa mot sinh vien (biet chinh xac ca diem va ten)
danh_sach_sv.remove((7.0, "Bình"))

# Sua diem cho sinh vien o vi tri xac dinh (vi du vi tri 0)
danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])

# Kiem tra mot sinh vien co trong danh sach hay khong
print("Chi co trong danh sach khong?", (9.2, "Chi") in danh_sach_sv)

# Sap xep theo diem tang dan (mac dinh so sanh phan tu dau tien cua tuple)
danh_sach_sv.sort()
print("\nDanh sach sau khi sap xep theo diem tang dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")

# Sap xep giam dan
danh_sach_sv.sort(reverse=True)
print("\nDanh sach sau khi sap xep theo diem giam dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")