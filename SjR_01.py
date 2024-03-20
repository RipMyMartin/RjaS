from MyModul import *

users = []
passwords = []

logPas = LoePasJaLog("autoriseerimine.txt")

kasutaja_registreeritud = False

while True:
    print(
        "\n0 - Registreerimine\n1 - Sisselogimine\n2 - Kasutajanime või parooli muutmine\n3 - Parooli taastamine\n4 - Väljumine"
    )

    valik: str = input("Sisestage valiku number: ")

    if valik == "4":
        break

    if valik == "0":
        kasutajanimi = input("Sisestage kasutajanimi: ")
        valik_parool = input("Kas soovite sisestada oma parooli (s) või genereerida süsteemi poolt (g)? ")
        if valik_parool.lower() == "s":
            parool = input("Sisestage parool: ")
        elif valik_parool.lower() == "g":
            parool = salasona(5)
            print("Genereeritud parool:", parool)
        registreeriKasutaja(kasutajanimi, parool, users, passwords)
        kasutaja_registreeritud = True

    elif valik == "1":
        kasutajanimi = input("Sisestage kasutajanimi: ")
        parool = input("Sisestage oma parool: ")
        sisselogimine(kasutajanimi, parool, logPas, users, passwords)

    elif valik == "2":
        kasutajanimi = input("Sisestage kasutajanimi: ")
        vanaParool = input("Sisestage vana parool: ")
        uusParool = input("Sisestage uus parool: ")
        muudaParool(kasutajanimi, vanaParool, uusParool)

    elif valik == "3":
        kasutajanimi = input("Sisestage kasutajanimi, kellele soovite parooli taastada: ")
        uusParool = input("Sisestage uus parool: ")
        unustatudParool(kasutajanimi, uusParool, logPas)
