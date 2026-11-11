import sqlite3

TEN_FILE_CSDL = "quan_ly_cong_viec.db"

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_nu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS cong_viec (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_cv TEXT NOT NULL,
            loai_cv TEXT NOT NULL,
            muc_do TEXT NOT NULL,
            so_gio REAL NOT NULL,
            trang_thai INTEGER NOT NULL DEFAULT 0
        )
    """)
    ket_noi.commit()
    ket_noi.close()

def them_cong_viec(ten_cv, loai_cv, muc_do, so_gio):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "INSERT INTO cong_viec (ten_cv, loai_cv, muc_do, so_gio, trang_thai) VALUES (?, ?, ?, ?, 0)",
        (ten_cv, loai_cv, muc_do, so_gio)
    )
    ket_noi.commit()
    ket_noi.close()

def lay_toan_bo_cong_viec():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, ten_cv, loai_cv, muc_do, so_gio, trang_thai FROM cong_viec ORDER BY id")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def xoa_cong_viec(id_cv):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM cong_viec WHERE id = ?", (id_cv,))
    ket_noi.commit()
    ket_noi.close()

def danh_dau_hoan_thanh(id_cv):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("UPDATE cong_viec SET trang_thai = 1 WHERE id = ?", (id_cv,))
    ket_noi.commit()
    ket_noi.close()

# Tên hàm đã được thống nhất chuẩn xác: thong_ke_theo_loai
def thong_ke_theo_loai():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT loai_cv, SUM(so_gio) FROM cong_viec GROUP BY loai_cv")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua