class Foglalas:

    def __init__(self):
        self.foglalasok = []

    def foglalas(self, szalloda, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas['szobaszam'] == szobaszam and foglalas['datum'] == datum:
                raise Exception("Ezen a napon a kiválasztott szoba már foglalt!")
        for szoba in szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                self.foglalasok.append({'szobaszam': szoba.szobaszam, 'datum': datum})
                return szoba.ar
        raise Exception("Nem létezik ilyen szoba!")

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas['szobaszam'] == szobaszam and foglalas['datum'] == datum:
                self.foglalasok.remove(foglalas)
                print("Foglalás lemondva.")
                return
        raise Exception("Nem létezik ilyen foglalás!")

    def foglalasok_listazasa(self):
        return self.foglalasok
