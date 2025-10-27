import math

class PhanSo:
    def __init__(self, tu_so, mau_so=1):
        """
        Khởi tạo phân số với tử số và mẫu số.
        Args:
            tu_so (int): Tử số của phân số.
            mau_so (int): Mẫu số của phân số. Mặc định là 1.
        """
        self._tu_so = tu_so
        self._mau_so = mau_so
        self._rut_gon()

    @property
    def tu_so(self):
        """
        Lấy tử số của phân số.
        Returns:
            int: Tử số của phân số.
         """
        return self._tu_so
    
    @tu_so.setter
    def tu_so(self, value):
        """
        Thiết lập tử số của phân số.
        Args:
            value (int): Tử số mới.
        """
        if not isinstance(value, int):
            raise ValueError("Tử số phải là số nguyên")
        self._tu_so = value

    @property
    def mau_so(self):
        """
        Lấy mẫu số của phân số.
        Returns:
            int: Mẫu số của phân số.
        """
        return self._mau_so
    
    @mau_so.setter
    def mau_so(self, value):
        """
        Thiết lập mẫu số của phân số.
        Args:
            value (int): Mẫu số mới.
        """
        if not isinstance(value, int):
            raise ValueError("Mẫu số phải là số nguyên")
        if value == 0:
            raise ValueError("Mẫu số không thể bằng 0")
        self._mau_so = value
    
    def _rut_gon(self):
        """
        Rút gọn phân số về dạng tối giản.
        """
        if hasattr(self, '_tu_so') and hasattr(self, '_mau_so'):
            gcd = math.gcd(abs(self._tu_so), abs(self._mau_so))
            self._tu_so //= gcd
            self._mau_so //= gcd

            if self._mau_so < 0:
                self._tu_so = -self._tu_so
                self._mau_so = -self._mau_so

    def rut_gon(self):
        """
        Rút gọn phân số về dạng tối giản.
        Returns:
            PhanSo: Phân số đã được rút gọn.
        """
        self._rut_gon()
        return self
    

    ### Toán tử số học
    def __add__(self, other):
        """Cộng hai phân số hoặc một phân số với một số nguyên/thực."""
        if isinstance(other, PhanSo):
            tu_moi = self.tu_so * other.mau_so + other.tu_so * self.mau_so
            mau_moi = self.mau_so * other.mau_so
            return PhanSo(tu_moi, mau_moi)
        elif isinstance(other, (int, float)):
            return self + PhanSo(int(other), 1)
        return NotImplemented
    
    def __radd__(self, other):
        """Phép cộng nghịch đảo"""
        return self.__add__(other)
    
    def __sub__(self, other):
        """Trừ hai phân số hoặc một phân số với một số nguyên/thực."""
        if isinstance(other, PhanSo):
            tu_moi = self.tu_so * other.mau_so - other.tu_so * self.mau_so
            mau_moi = self.mau_so * other.mau_so
            return PhanSo(tu_moi, mau_moi)
        elif isinstance(other, (int, float)):
            return self - PhanSo(int(other), 1)
        return NotImplemented
    
    def __rsub__(self, other):
        """Phép trừ nghịch đảo"""
        if isinstance(other, (int, float)): 
            return PhanSo(int(other), 1) - self
        return NotImplemented
    
    def __mul__(self, other):
        """Nhân hai phân số hoặc một phân số với một số nguyên/thực."""
        if isinstance(other, PhanSo):
            tu_moi = self.tu_so * other.tu_so
            mau_moi = self.mau_so * other.mau_so
            return PhanSo(tu_moi, mau_moi)
        elif isinstance(other, (int, float)):
            return self * PhanSo(int(other), 1)
        return NotImplemented
    
    def __rmul__(self, other):
        """Phép nhân nghịch đảo"""
        return self.__mul__(other)
    
    def __truediv__(self, other):
        """Chia hai phân số hoặc một phân số với một số nguyên/thực."""
        if isinstance(other, PhanSo):
            if other.tu_so == 0:
                raise ZeroDivisionError("Không thể chia cho phân số có tử số bằng 0")
            tu_moi = self.tu_so * other.mau_so
            mau_moi = self.mau_so * other.tu_so
            return PhanSo(tu_moi, mau_moi)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Không thể chia cho 0")
            return self / PhanSo(1, int(other))
        return NotImplemented
    
    def __rtruediv__(self, other):
        """Phép chia nghịch đảo"""
        if isinstance(other, (int, float)):
            return PhanSo(int(other), 1) / self
        return NotImplemented
    
    ### Toán tử so sánh

    def __eq__(self, other):
        """So sánh hai phân số hoặc một phân số với một số nguyên/thực."""
        if isinstance(other, PhanSo):
            return self.tu_so * other.mau_so == self.mau_so * other.tu_so
        elif isinstance(other, (int, float)):
            return self == PhanSo(int(other), 1)
        return False
    
    def __ne__(self, other):
        """So sánh không bằng hai phân số hoặc một phân số với một số nguyên/thực."""
        return not self.__eq__(other)
    
    def __lt__(self, other):
        """So sánh hai phân số hoặc một phân số với một số nguyên/thực."""
        if isinstance(other, PhanSo):
            return self.tu_so * other.mau_so < self.mau_so * other.tu_so
        elif isinstance(other, (int, float)):
            return self < PhanSo(int(other), 1)
        return False
    
    def __le__(self, other):
        """So sánh nhỏ hơn hoặc bằng hai phân số hoặc một phân số với một số nguyên/thực."""
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other):
        """So sánh hai phân số hoặc một phân số với một số nguyên/thực."""
        if isinstance(other, PhanSo):
            return self.tu_so * other.mau_so > self.mau_so * other.tu_so
        elif isinstance(other, (int, float)):
            return self > PhanSo(int(other), 1)
        return False
    
    def __ge__(self, other):
        """So sánh lớn hơn hoặc bằng hai phân số hoặc một phân số với một số nguyên/thực."""
        return self.__gt__(other) or self.__eq__(other)
    
    ### Hiện thị

    def __str__(self):
        """Hiển thị phân số dưới dạng chuỗi."""
        if self.mau_so == 1:
            return str(self.tu_so)
        return f"{self.tu_so} / {self.mau_so}"
    
    def __repr__(self):
        """Hiển thị phân số dưới dạng chuỗi cho mục đích gỡ lỗi."""
        return f"PhanSo({self.tu_so}, {self.mau_so})"

    
        