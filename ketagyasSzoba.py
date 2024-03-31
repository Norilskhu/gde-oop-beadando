from szoba import Szoba


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, agy_meret):
        self.agy_meret = agy_meret
        super().__init__(20000, szobaszam)
