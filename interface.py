from datetime import datetime


def datum_valaszto():
    while True:
        datum = input("Adja meg a foglalás dátumát az alábbi formátumban: 'YYYY-MM-DD'")
        try:
            formatted_datum = datetime.strptime(datum, '%Y-%m-%d').date()
            if formatted_datum <= datetime.now().date():
                print('A megadott dátum nem jövőbeli. Kérem adjon meg egy jövőbeli dátumot!')
            else:
                return datum
        except ValueError:
            print("Hibás dátumformátum. Próbálja újra!")


def print_interface(szalloda, foglalas):
    print("\nÜdvözöljük a Hotel Fonyód foglalási rendszerében! \n\nKérjük válasszon az alábbiak közül:")
    while True:
        print("\n1. Foglalás\n"
              "2. Lemondás\n"
              "3. Foglalások listázása\n"
              "4. Kilépés")
        input_code = input("> ")

        match input_code:
            case "1":
                szobaszam = input("Kérem adja meg a lefoglalni kívánt szoba szobaszámát: ")
                datum = datum_valaszto()
                try:
                    ar = foglalas.foglalas(szalloda, szobaszam, datum)
                    print("Sikeres foglalás! A szoba ára: " + str(ar) + " forint.")
                except Exception as e:
                    print(e)
            case "2":
                szobaszam = input("Kérem adja meg a lemondani kívánt szoba szobaszámát: ")
                datum = datum_valaszto()
                try:
                    foglalas.lemondas(szobaszam, datum)
                except Exception as e:
                    print(e)
            case "3":
                print("Rendszerünkben az alábbi foglalások találhatóak: \n")
                foglalasok = foglalas.foglalasok_listazasa()
                for foglalas_dict in foglalasok:
                    print("Szobaszám: " + str(foglalas_dict['szobaszam']) + " --- lefoglalt dátum: " + foglalas_dict['datum'])
            case "4":
                print("Shutting down...")
                break
