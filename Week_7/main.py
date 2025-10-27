from Phanso import PhanSo
from func import nhap_phan_so, nhap_phep_toan, thuc_hien_phep_toan, hien_thi_ket_qua, hien_thi_menu, so_sanh_phan_so

def main():
    hien_thi_menu()

    while True:
        try:
            lua_chon = input("Chọn chức năng (1-5): ").strip()

            if lua_chon == '1':
                print("\nNhập phân số thứ nhất:")
                phan_so1 = nhap_phan_so()
                print("\nNhập phân số thứ hai:")
                phan_so2 = nhap_phan_so()
                print("--------------------------------\n")
            elif lua_chon == '2':
                phep_toan = nhap_phep_toan()
                print("--------------------------------\n")
            elif lua_chon == '3':
                try:
                    ket_qua = thuc_hien_phep_toan(phan_so1, phan_so2, phep_toan)
                    hien_thi_ket_qua(phan_so1, phan_so2, phep_toan, ket_qua)
                    print("--------------------------------\n")
                except NameError:
                    print("Lỗi: Vui lòng nhập hai phân số và chọn phép toán trước khi thực hiện.")
                except Exception as e:
                    print(e)
            elif lua_chon == '4':
                try:
                    so_sanh_phan_so(phan_so1, phan_so2)
                    print("--------------------------------\n")
                except NameError:
                    print("Lỗi: Vui lòng nhập hai phân số trước khi so sánh.")
            elif lua_chon == '5':
                print("Thoát chương trình. Tạm biệt!")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        except KeyboardInterrupt:
            print("\nThoát chương trình. Tạm biệt!")
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    main()

        
            
                