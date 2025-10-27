from Phanso import PhanSo

def nhap_phan_so():
    """
    Hàm nhập phân số từ người dùng.
    Returns:
        PhanSo: Đối tượng phân số được tạo từ dữ liệu nhập vào.
    """
    while True:
        try:
            tu_so = int(input("Nhập tử số: "))
            mau_so = int(input("Nhập mẫu số: "))
            phan_so = PhanSo(tu_so, mau_so)
            return phan_so
        except ValueError as e:
            print(f"Lỗi: {e}. Vui lòng nhập lại.")
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}. Vui lòng nhập lại.")

def nhap_phep_toan():
    """
    Hàm nhập phép toán từ người dùng.
    Returns:
        str: Phép toán được nhập vào.
    """
    while True:
        phep_toan = input("Nhập phép toán (+, -, *, /): ")
        if phep_toan in ['+', '-', '*', '/']:
            return phep_toan
        else:
            print("Phép toán không hợp lệ. Vui lòng nhập lại.")

def thuc_hien_phep_toan(phan_so1, phan_so2, phep_toan):
    """
    Hàm thực hiện phép toán trên hai phân số.
    Args:
        phan_so1 (PhanSo): Phân số thứ nhất.
        phan_so2 (PhanSo): Phân số thứ hai.
        phep_toan (str): Phép toán cần thực hiện.
    Returns:
        PhanSo: Kết quả của phép toán.
    """
    try:
        if phep_toan == '+':
            return phan_so1 + phan_so2
        elif phep_toan == '-':
            return phan_so1 - phan_so2
        elif phep_toan == '*':
            return phan_so1 * phan_so2
        elif phep_toan == '/':
            return phan_so1 / phan_so2
    except ZeroDivisionError as e:
        raise ZeroDivisionError("Lỗi: Chia cho phân số bằng 0 không hợp lệ.")
    except Exception as e:
        raise Exception(f"Có lỗi xảy ra khi thực hiện phép toán: {e}")
    
def hien_thi_ket_qua(phan_so1, phan_so2, phep_toan, ket_qua):
    """
    Hàm hiển thị kết quả của phép toán.
    Args:
        phan_so1 (PhanSo): Phân số thứ nhất.
        phan_so2 (PhanSo): Phân số thứ hai.
        phep_toan (str): Phép toán đã thực hiện.
        ket_qua (PhanSo): Kết quả của phép toán.
    """
    print(f"\n" + "="*30)
    print("Kết quả phép toán:")
    print(f"{phan_so1} {phep_toan} {phan_so2} = {ket_qua}")
    print("\n" + "="*30 + "\n")

def so_sanh_phan_so(phan_so1, phan_so2):
    """
    Hàm so sánh hai phân số và hiển thị kết quả.
    Args:
        phan_so1 (PhanSo): Phân số thứ nhất.
        phan_so2 (PhanSo): Phân số thứ hai.
    """
    print(f"\n" + "="*30)
    print(f"\nSo sánh phân số:")
    print(f"  {phan_so1} == {phan_so2}  ➜  {phan_so1 == phan_so2}")
    print(f"  {phan_so1} != {phan_so2}  ➜  {phan_so1 != phan_so2}")
    print(f"  {phan_so1} <  {phan_so2}  ➜  {phan_so1 < phan_so2}")
    print(f"  {phan_so1} <= {phan_so2}  ➜  {phan_so1 <= phan_so2}")
    print(f"  {phan_so1} >  {phan_so2}  ➜  {phan_so1 > phan_so2}")
    print(f"  {phan_so1} >= {phan_so2}  ➜  {phan_so1 >= phan_so2}")
    print("\n" + "="*30 + "\n")

def hien_thi_menu():
    """
    Hàm hiển thị menu chính của chương trình.
    """
    print("\n" + "="*40)
    print("Chương trình Phép Toán Trên Phân Số")
    print("1. Nhập hai phân số")
    print("2. Chọn phép toán (+, -, *, /)")
    print("3. Thực hiện phép toán và hiển thị kết quả")
    print("4. So sánh hai phân số")
    print("5. Thoát chương trình")
    print("="*40 + "\n")

    