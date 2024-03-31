from egyagyasSzoba import EgyagyasSzoba
from foglalas import Foglalas
from ketagyasSzoba import KetagyasSzoba
from szalloda import Szalloda


class Loader:
    def self_load(self):
        egyagyas_szoba_foldszint = EgyagyasSzoba("101", "0")
        egyagyas_szoba_emelet = EgyagyasSzoba("201", "1")
        ketagyas_szoba = KetagyasSzoba("222", "king_size")

        self.szalloda.szoba_hozzaadasa(egyagyas_szoba_foldszint)
        self.szalloda.szoba_hozzaadasa(egyagyas_szoba_emelet)
        self.szalloda.szoba_hozzaadasa(ketagyas_szoba)

        self.foglalas.foglalas(self.szalloda, "101", "2024-08-20")
        self.foglalas.foglalas(self.szalloda,  "201", "2024-08-20")
        self.foglalas.foglalas(self.szalloda, "222", "2024-08-20")
        self.foglalas.foglalas(self.szalloda,  "101", "2024-08-21")
        self.foglalas.foglalas(self.szalloda,  "101", "2024-08-22")

    def __init__(self):
        self.szalloda = Szalloda()
        self.foglalas = Foglalas()
        self.self_load()
