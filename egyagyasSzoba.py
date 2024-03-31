from szoba import Szoba


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, emelet):
        self.emelet = emelet
        super().__init__(10000, szobaszam)
