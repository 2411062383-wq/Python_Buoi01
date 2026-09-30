# HOẠT ĐỘNG 1: Hàm cơ bản – def, tham số, return
# Bài tập 1.1: Viết hàm và gọi lại nhiều lần (ít nhất 3 bộ dữ liệu)

def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bscnn(a, b):
    return a * b // uscln(a, b)

def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

print("--- KIỂM THỬ HOẠT ĐỘNG 1 ---")
# Gọi thử với ít nhất 3 bộ dữ liệu khác nhau
print("USCLN(24, 36):", uscln(24, 36))
print("USCLN(17, 13):", uscln(17, 13))
print("USCLN(100, 25):", uscln(100, 25))

print("BSCNN(4, 6):", bscnn(4, 6))
print("BSCNN(5, 7):", bscnn(5, 7))
print("BSCNN(12, 18):", bscnn(12, 18))

print("Kiem tra nguyen to (29):", kiem_tra_nguyen_to(29))
print("Kiem tra nguyen to (15):", kiem_tra_nguyen_to(15))
print("Kiem tra nguyen to (2):", kiem_tra_nguyen_to(2))

print("Kiem tra so hoan thien (28):", kiem_tra_so_hoan_thien(28))
print("Kiem tra so hoan thien (6):", kiem_tra_so_hoan_thien(6))
print("Kiem tra so hoan thien (12):", kiem_tra_so_hoan_thien(12))

# Bài tập 1.2 – return không giá trị và trả về nhiều giá trị

def in_loi_chao(ten):
    print(f"Xin chao, {ten}!")
    return 

def chia_lay_thuong_du(a, b):

    return a // b, a % b  
print("\n--- KIỂM THỬ BÀI TẬP 1.2 ---")
in_loi_chao("An")
thuong, du = chia_lay_thuong_du(17, 5)
print(f"Thuong: {thuong}, du: {du}")

# HOẠT ĐỘNG 2: Tham số mặc định & tham số từ khóa

def gioi_thieu(ten, tuoi=18, lop="Chua ro"):
    print(f"Ten: {ten} - Tuoi: {tuoi} - Lop: {lop}")

print("\n--- KIỂM THỬ HOẠT ĐỘNG 2 ---")
gioi_thieu("An")                                      
gioi_thieu("Binh", 20)                             
gioi_thieu("Chi", lop="CNTT01")                       
gioi_thieu(ten="Dung", lop="CNTT02", tuoi=19)        

# HOẠT ĐỘNG 3: Tham số linh hoạt – *args và **kwargs
# Bài tập 3.1 – *args: tính tổng số lượng bất kỳ các số

def tinh_tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong

print("\n--- KIỂM THỬ BÀI TẬP 3.1 ---")
print("Tong (1, 2, 3):", tinh_tong(1, 2, 3))
print("Tong (5, 10, 15, 20, 25):", tinh_tong(5, 10, 15, 20, 25))
print("Tong ():", tinh_tong())  

# Bài tập 3.2 – **kwargs: in thông tin động

def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"Ho ten: {ho_ten} - Tuoi: {tuoi}")
    for khoa, gia_tri in kwargs.items():
        print(f"  {khoa}: {gia_tri}")

print("\n--- KIỂM THỬ BÀI TẬP 3.2 ---")
in_thong_tin("Nguyen Van A", 20, lop="CNTT01", que_quan="Ha Noi")
in_thong_tin("Tran Thi B", 21, email="b@example.com")