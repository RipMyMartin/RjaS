import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string


def registreeriKasutaja(kasutajanimi, parool, kasutajad, paroolid):
    """Funktsioon kasutaja registreerimiseks."""
    kasutajad.append(kasutajanimi)
    paroolid.append(parool)

    # Uue kasutaja kirjutamine faili
    with open("autoriseerimine.txt", "a", encoding="utf-8") as f:
        f.write(f"{kasutajanimi}:{parool}\n")

    print("Kasutaja on edukalt registreeritud.")


def LoePasJaLog(fail: str) -> any:
    """Andmete lugemine failist ja sõnastiku loomine."""
    logPas = {}
    with open(fail, "r", encoding="utf-8") as f:
        for line in f:
            l, p = line.strip().split(":")
            logPas[l] = p
    return logPas


def salasona(pikkus: int):
    """Funktsioon genereerib juhusliku parooli."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(pikkus))


def muudaParool(kasutajanimi, vanaParool, uusParool):
    """Funktsioon kasutaja parooli muutmiseks autoriseerimisfailis."""""
    # Kõigepealt loeme vanu andmeid
    with open("autoriseerimine.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open("autoriseerimine.txt", "w", encoding="utf-8") as f:
        for line in lines:
            user, password = line.strip().split(":")
            if user == kasutajanimi:
                f.write(f"{kasutajanimi}:{uusParool}\n")
            else:
                f.write(line)

    print("Parool on edukalt muudetud.")




def kirjutaFailisse(fail: str, jarjend):
    """Faili kirjutamine antud järjendi sisuga."""
    with open(fail, "w", encoding="utf-8") as f:
        for el in jarjend:
            f.write(el + "\n")


def sisselogimine(kasutajanimi, parool, logPas, kasutajad, paroolid):
    """Funktsioon kontrollib kasutajanime ja parooli sisselogimisel."""
    if not kasutajanimi or not parool:
        print("Palun sisestage nii kasutajanimi kui ka parool.")
        return

    if kasutajanimi in logPas:
        if parool == logPas[kasutajanimi]:
            print("Sisselogimine õnnestus.")
        else:
            print("Vale parool.")
    else:
        print("Kasutajanime ei eksisteeri.")


def unustatudParool(kasutajanimi: str, uusParool: str, logPas: dict):
    """Funktsioon saadab kasutajale e-kirja uue parooliga."""
    if kasutajanimi in logPas:
        logPas[kasutajanimi] = uusParool

        with open("autoriseerimine.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        with open("autoriseerimine.txt", "w", encoding="utf-8") as f:
            for line in lines:
                user, password = line.strip().split(":")
                if user == kasutajanimi:
                    f.write(f"{user}:{uusParool}\n")
                else:
                    f.write(line)

        # Kirja saatmine
        try:
            context = ssl.create_default_context()
            smtp_server = "smtp.gmail.com"
            port = 587
            sender_email = "martinsild.mr@gmail.com"
            receiver_email = input("Sisesta oma emaili aadress: ")
            password = input("Type your password and press enter: ")
            subject = "Unustatud parool"
            body = f"Teie kasutaja nimi {kasutajanimi}\nTeie unustatud parool on: {uusParool}"

            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))
            msg = message.as_string()

            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg)
            print("Unustatud parool on saadetud teie email")
        except Exception as e:
            print("Viga kirja saatmisel:", str(e))
        finally:
            server.quit()

        print("Parool on edukalt muudetud. Uus parool on saadetud märgitud e-posti aadressile.")
    else:
        print("Kasutajat määratud nimega ei leitud.")









