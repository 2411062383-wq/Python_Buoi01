import math

# ==========================================
# HOẠT ĐỘNG 4: TUPLE - KHAI BÁO, BẤT BIẾN, UNPACKING
# ==========================================
print("=== HOẠT ĐỘNG 4 ===")

# Bài tập 4.1 - Khai báo & tính bất biến
toa_do = (3, 5)
print(toa_do, type(toa_do))


# Bài tập 4.2 - Unpacking tuple
x, y = toa_do
print("x =", x, "- y =", y)

# Đổi giá trị 2 biến bằng unpacking (không cần biến tạm)
a, b = 10, 20
a, b = b, a
print("a =", a, "- b =", b)

# Bài tập 4.3 - Trả về nhiều giá trị từ một biểu thức
c, d = 17, 5
thuong_du = divmod(c, d)      # divmod tra ve mot tuple (thuong, du)
thuong, du = thuong_du        # unpacking ket qua
print(f"{c} chia {d} duoc thuong {thuong}, du {du}")

print("\n" + "="*40 + "\n")

# ==========================================
# HOẠT ĐỘNG 5: VẬN DỤNG TUPLE - TỌA ĐỘ ĐIỂM & KHOẢNG CÁCH
# ==========================================
print("=== HOẠT ĐỘNG 5 ===")

diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

print("-" * 30)

# --- YÊU CẦU BÀI TẬP HOẠT ĐỘNG 5: TÍNH KHOẢNG CÁCH CÁC ĐIỂM VỚI GỐC TỌA ĐỘ (0,0) ---
cac_diem = [(0, 0), (3, 4), (6, 8)]

for diem in cac_diem:
    x, y = diem
    dist = math.sqrt(x**2 + y**2)
    print(f"Khoang cach tu {diem} den goc toa do (0,0) la: {round(dist, 2)}")