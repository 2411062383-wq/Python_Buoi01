import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import csdl_cong_viec as db

DANH_SACH_LOAI = ["Hoc tap", "Lap trinh", "The thao", "Giai tri", "Khac"]
DANH_SACH_MUC_DO = ["Thap", "Trung binh", "Cao"]

class UngDungQuanLyCongViec(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Thoi gian & Cong viec")
        self.geometry("620x520")
        self.resizable(False, False)

        db.tao_bang_nu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def khoi_tao_giao_dien(self):
        khung_nhap = tk.LabelFrame(self, text=" Thong tin cong viec moi ", padx=10, pady=10)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Ten cong viec:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_ten_cv = tk.Entry(khung_nhap, width=32)
        self.o_ten_cv.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Loai cong viec:").grid(row=1, column=0, sticky="w", pady=5)
        self.chon_loai = ttk.Combobox(khung_nhap, values=DANH_SACH_LOAI, width=30, state="readonly")
        self.chon_loai.current(0)
        self.chon_loai.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Muc do uu tien:").grid(row=2, column=0, sticky="w", pady=5)
        self.chon_muc_do = ttk.Combobox(khung_nhap, values=DANH_SACH_MUC_DO, width=30, state="readonly")
        self.chon_muc_do.current(1)
        self.chon_muc_do.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="So gio du kien:").grid(row=3, column=0, sticky="w", pady=5)
        self.o_so_gio = tk.Entry(khung_nhap, width=32)
        self.o_so_gio.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(khung_nhap, text="Them cong viec", bg="lightgreen", command=self.xu_ly_them).grid(row=4, column=0, columnspan=2, pady=10)

        # Khung danh sách
        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox = tk.Listbox(khung_danh_sach, width=82, height=12)
        self.listbox.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=thanh_cuon.set)

        # Khung nút chức năng
        khung_nut = tk.Frame(self)
        khung_nut.pack(pady=10)

        tk.Button(khung_nut, text="Danh dau Da hoan thanh", command=self.xu_ly_hoan_thanh).grid(row=0, column=0, padx=5)
        tk.Button(khung_nut, text="Xoa cong viec", fg="red", command=self.xu_ly_xoa).grid(row=0, column=1, padx=5)
        tk.Button(khung_nut, text="Thong ke Tong so gio", bg="lightblue", command=self.xu_ly_thong_ke).grid(row=0, column=2, padx=5)

    def tai_lai_danh_sach(self):
        self.listbox.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_cong_viec()

        for cv in self.danh_sach_hien_tai:
            id_cv, ten_cv, loai_cv, muc_do, so_gio, trang_thai = cv
            trang_thai_str = "[Da xong]" if trang_thai == 1 else "[Dang lam]"
            self.listbox.insert(tk.END, f"{trang_thai_str} {ten_cv} | Loai: {loai_cv} | Uu tien: {muc_do} | Thoi gian: {so_gio}h")

    def xu_ly_them(self):
        ten = self.o_ten_cv.get().strip()
        loai = self.chon_loai.get()
        muc_do = self.chon_muc_do.get()
        str_gio = self.o_so_gio.get().strip()

        if not ten or not str_gio:
            messagebox.showerror("Loi", "Vui long nhap day du ten cong viec va so gio!")
            return

        try:
            so_gio = float(str_gio)
        except ValueError:
            messagebox.showerror("Loi", "So gio phai la mot so hop le!")
            return

        db.them_cong_viec(ten, loai, muc_do, so_gio)
        self.o_ten_cv.delete(0, tk.END)
        self.o_so_gio.delete(0, tk.END)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thanh cong", f"Da them cong viec: {ten}")

    def xu_ly_xoa(self):
        lua_chon = self.listbox.curselection()
        if not lua_chon:
            messagebox.showerror("Loi", "Vui long chon mot cong viec de xoa.")
            return
        id_cv = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_cong_viec(id_cv)
        self.tai_lai_danh_sach()

    def xu_ly_hoan_thanh(self):
        lua_chon = self.listbox.curselection()
        if not lua_chon:
            messagebox.showerror("Loi", "Vui long chon mot cong viec de danh dau hoan thanh.")
            return
        id_cv = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.danh_dau_hoan_thanh(id_cv)
        self.tai_lai_danh_sach()

    def xu_ly_thong_ke(self):
        # Gọi chính xác tên hàm thong_ke_theo_loai đã đồng bộ
        data = db.thong_ke_theo_loai()
        if not data:
            messagebox.showinfo("Thong bao", "Chua co du lieu de thong ke.")
            return

        loai_list = [row[0] for row in data]
        gio_list = [row[1] for row in data]

        plt.figure(figsize=(6, 4))
        plt.bar(loai_list, gio_list, color="teal")
        plt.title("Tong so gio danh cho tung loai cong viec")
        plt.xlabel("Loai cong viec")
        plt.ylabel("So gio (h)")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = UngDungQuanLyCongViec()
    app.mainloop()