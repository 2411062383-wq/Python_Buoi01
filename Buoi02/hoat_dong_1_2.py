# Bài tập 1.1 - input() và ép kiểu
ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))
# Bài tập 1.2 - print() với sep/end
print("Python", "la", "ngon", "ngu", "lap trinh", sep="-")
print("Dong 1", end=" | ")
print("Dong 2")
# Thử đổi sep thành nhiều ký tự khác nhau:
print("\n--- Thu nghiem voi cac sep khac nhau ---")
print("Python", "la", "ngon", "ngu", "lap trinh", sep=", ")
print("Python", "la", "ngon", "ngu", "lap trinh", sep="")
print("Python", "la", "ngon", "ngu", "lap trinh", sep="\n")
# Bài tập 1.3 - So sánh 3 cách định dạng chuỗi
print("\n--- In ket qua Bài 1.1 bằng 3 cach ---")
# 1. f-string
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")
# 2. str.format()
print("Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(ho_ten, nam_sinh, diem_tb))
# 3. Toán tử %
print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" % (ho_ten, nam_sinh, diem_tb))
# Bài tập 2.1 - Chú thích
# Chu thich mot dong: khai bao thong tin sinh vien
"""
Chu thich/docstring nhieu dong:
Chuong trinh quan ly diem sinh vien - Buoi 2
"""
ho_ten_sv = "Tran Thi B"  # bien luu ho ten

# Bài tập 2.2 - Các kiểu trích dẫn & escape
s1 = 'Xin chao'
s2 = "Ban co khoe khong?"
s3 = '''Day la
mot chuoi
nhieu dong'''
s4 = "Duong dan: C:\\Python\\data"
s5 = r"Duong dan raw: C:\Python\data"
s6 = "Toi ten la \"Nam\", con ban ten gi?"

print("\n--- In ket qua Bai 2.2 ---")
print(s1); print(s2); print(s3); print(s4); print(s5); print(s6)