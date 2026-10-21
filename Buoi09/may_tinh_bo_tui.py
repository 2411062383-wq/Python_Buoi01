import tkinter as tk
from tkinter import messagebox

def nhap_ky_tu(ky_tu):
    bieu_thuc_hien_tai = bien_bieu_thuc.get()
    bien_bieu_thuc.set(bieu_thuc_hien_tai + str(ky_tu))

def xoa_man_hinh():
    bien_bieu_thuc.set("")

def tinh_ket_qua():
    try:
        ket_qua = str(eval(bien_bieu_thuc.get()))
        bien_bieu_thuc.set(ket_qua)
    except Exception:
        messagebox.showerror("Loi", "Bieu thuc khong hop le!")
        bien_bieu_thuc.set("")

# Khoi tao cua so
cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("300x350")
cua_so.resizable(False, False)

bien_bieu_thuc = tk.StringVar()

# Man hinh hien thi
man_hinh = tk.Entry(cua_so, textvariable=bien_bieu_thuc, font=("Arial", 18), justify="right", bd=10)
man_hinh.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

# Danh sach cac nut
nut_bam = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2)
]

for (text, row, col) in nut_bam:
    action = lambda x=text: nhap_ky_tu(x)
    tk.Button(cua_so, text=text, font=("Arial", 14), width=5, height=2, command=action).grid(row=row, column=col, padx=2, pady=2)

# Nut Xoa (C) va Nut Bang (=)
tk.Button(cua_so, text="C", font=("Arial", 14), width=5, height=2, command=xoa_man_hinh).grid(row=4, column=3, padx=2, pady=2)
tk.Button(cua_so, text="=", font=("Arial", 14), width=24, height=2, bg="lightblue", command=tinh_ket_qua).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

cua_so.mainloop()