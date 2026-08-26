import math
# Bài tập 3.1 - Các kiểu số & chuyển đổi
so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j

print(type(so_nguyen), type(so_thuc), type(so_phuc))
print(float(so_nguyen))  # ep int -> float
print(int(so_thuc))      # ep float -> int (cat phan thap phan)

# Bài tập 3.2 – Hàm built-in xử lý số
a = -7
b = 2.6789
c, d = 17, 5

print("\n--- Kế quả Bài 3.2 ---")
print(abs(a))           # Gia tri tuyet doi
print(round(b))         # Lam tron
print(round(b, 2))      # Lam tron 2 chu so thap phan
print(pow(c, 2))        # c mu 2
print(divmod(c, d))     # Tra ve (thuong, du) dang tuple
# Bài tập 3.3 - Vận dụng: Tính nghiệm phương trình bậc hai
a_pt, b_pt, c_pt = 1, -3, 2
delta = b_pt ** 2 - 4 * a_pt * c_pt
x1 = (-b_pt + math.sqrt(delta)) / (2 * a_pt)
x2 = (-b_pt - math.sqrt(delta)) / (2 * a_pt)

print(f"\nDelta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")
# Bài tập 4.1 - Indexing & slicing
cau = "Lap trinh Python rat thu vi"

print("\n--- Ket qua Bài 4.1 ---")
print(cau[0])         # Ky tu dau tien
print(cau[-1])        # Ky tu cuoi cung
print(cau[4:10])      # Cat tu vi tri 4 den truoc vi tri 10
print(cau[:8])        # Tu dau den vi tri 8
print(cau[11:])       # Tu vi tri 11 den het
print(cau[::-1])      # Dao nguoc chuoi

# Kiểm tra Palindrome
is_palindrome = (cau == cau[::-1])
print(f"Chuoi '{cau}' co phai Palindrome hay khong? {is_palindrome}")

# Bài tập 4.2 - Tính bất biến (immutable)
ten = "Nam"
# ten[0] = "T" -> TypeError: 'str' object does not support item assignment
ten_moi = "T" + ten[1:]
print(f"Ten sau khi sua: {ten_moi}")

# Bài tập 4.3 - Các phương thức xử lý chuỗi thường dùng
cau_str = "  Toi dang HOC Python rat vui  "

print("\n--- Ket qua Bài 4.3 ---")
print(cau_str.strip())                                  # Bo khoang trang 2 dau
print(cau_str.strip().upper())                          # In hoa toan bo
print(cau_str.strip().lower())                          # In thuong toan bo
print(cau_str.strip().replace("HOC", "hoc"))            # Thay the chuoi
print(cau_str.strip().split())                          # Tach thanh danh sach cac tu
print(len(cau_str.strip().split()))                     # Dem so tu trong cau
print(cau_str.count("o"))                               # Dem so lan xuat hien ky tu 'o'
print(cau_str.find("Python"))                           # Vi tri bat dau cua "Python"
print(cau_str.strip().startswith("Toi"))                # Kiem tra bat dau
print(cau_str.strip().endswith("vui"))                  # Kiem tra ket thuc
print("-".join(["Python", "that", "thu", "vi"]))        # Noi chuoiBang dau '-'

# Bài tập 4.4 - Vận dụng: Chuẩn hóa họ tên
ho_ten_tho = "   nguyen   van   an  "
ho_ten_sach = " ".join(ho_ten_tho.split()).title()
print(f"\nHo ten sach: {ho_ten_sach}")
