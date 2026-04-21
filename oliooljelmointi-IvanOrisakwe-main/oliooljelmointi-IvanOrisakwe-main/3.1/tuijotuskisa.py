import random
import time

class Olento:
    """Kantaluokka, joka kuvaa oliota (Peikko tai Sankari)."""

    def __init__(self, nimi, rohkeus, katseen_voima):
        self.__nimi = nimi
        self.__rohkeus = rohkeus
        self.__katseen_voima = katseen_voima


    def hae_nimi(self):
        return self.__nimi
    def aseta_nimi(self, arvo):
        self.__nimi = str(arvo)
    def hae_rohkeus(self):
        return self.__rohkeus

    def aseta_rohkeus(self, arvo):
        self.__rohkeus = int(arvo)

    def hae_katseen_voima(self):
        return self.__katseen_voima

    def aseta_katseen_voima(self, arvo):
        self.__katseen_voima = int(arvo)


    def arvo_hurraus(self):
        """Perus-implementaatio (ylikirjoitetaan aliluokissa)."""
        return "Hurraa!"

class Peikko(Olento):
    """Luokka, joka kuvaa Peikon."""
    NIMITAVUT = ("Ur", "Gar", "Grah", "Gur", "Kan", "Kazah", "Bar", "Bazh", "Ragh", "Rudz")
    RIEMUTAVUT = ("Agh", "Ugh", "Ourgh", "Drar", "Brar", "Dza", "Gra", "Gur", "Rah", "Urgh", "Ra")

    def __init__(self):
        """Peikko-luokan konstruktori."""
        nimi = self._arvo_sanat(self.NIMITAVUT, 3, "-")
        # Arvotaan ominaisuudet aiotuilta väleiltä: rohkeus 4-8, katseen_voima 2-4
        super().__init__(nimi, random.randint(4, 8), random.randint(2, 4))

    def _arvo_sanat(self, tavut, n, erotin, p=0.5):
        """Muodostaa satunnaisen tekstin annetuista tavuista."""
        osat = random.choices(tavut, k=random.randint(2, n))
        sanat = osat[0]
        for osa in osat[1:]:
            if random.random() < p:
                sanat += erotin + osa
            else:
                sanat += osa.lower()
        return sanat

    def arvo_hurraus(self):
        """Palauttaa satunnaisen hurraushuudahduksen."""
        return self._arvo_sanat(self.RIEMUTAVUT, 8, " ", 0.7)

class Sankari(Olento):
    def __init__(self, nimi):
        """Sankari-luokan konstruktori."""
        Olento.__init__(self, nimi, random.randint(5, 10), random.randint(3, 6))

    def arvo_hurraus(self):
        """Palauttaa satunnaisen hurrauksen."""
        words = ["Hooray!", "Leart!", "6..7!", "wooooo!", "fyn shyt!"]
        return random.choice(words)

class Vuorenpeikko(Peikko):
    """Kuvaa vuorenpeikkoa."""
    VUORI_NIMITAVUT = ("Krag", "Thur", "Grim", "Kor", "Barg", "Drak", "Mor", "Skar", "Tor", "Vrak")
    VUORI_RIEMUTAVUT = ("GRAAAH", "THUUUM", "KRAAGH", "ROOAAR", "THUUUGH", "GRRRR", "BRAAGH", "HOOOOM")

    def __init__(self):
        nimi = self._arvo_sanat(self.VUORI_NIMITAVUT, 7, "-")
        # Rohkeus 6-10, katseen_voima 5-7
        super(Olento, self).__init__()  # varmistetaan ettei Peikon __init__ arvo pinto uudelleen
        Olento.__init__(self, nimi, random.randint(6, 10), random.randint(5, 7))

    def arvo_hurraus(self):
        return self._arvo_sanat(self.VUORI_RIEMUTAVUT, 4, " ", 0.4)

class Luolapeikko(Peikko):
    """Kuvaa luolapeikkoa."""
    NIMITAVUT = ("Gob", "Snag", "Grik", "Mok", "Zag", "Nok", "Gur", "Skab", "Vek", "Zok")
    RIEMUTAVUT = ("hihihi", "kekeke", "hehehe", "gigigi", "kukuku", "sisisi", "tihihi")

    def __init__(self):
        nimi = self._arvo_sanat(self.NIMITAVUT, 2, "")

        super(Olento, self).__init__()  
        Olento.__init__(self, nimi, random.randint(5, 9), random.randint(4, 6))

    def arvo_hurraus(self):
        return self._arvo_sanat(self.RIEMUTAVUT, 6, " ", 0.8)

def hurraa(olio):
    """Tulostaa satunnaisen hurrauksen annetulle oliolle."""
    print(f'{olio.hae_nimi()}: "{olio.arvo_hurraus()}!"')

def tulosta_rapaytys(rapayttaja):
    """Tulostaa sopivan tekstin räpäyttävälle oliolle."""
    if rapayttaja:
        if rapayttaja.hae_rohkeus() > 0:
            print(f"ja {rapayttaja.hae_nimi()} räpäyttää!")
        else:
            print(f"ja {rapayttaja.hae_nimi()} karkaa!")
    else:
        print("eikä kummankaan silmä rävähdä!")

def tuijota(olio1, olio2):
    """Asettaa annetut oliot taistelemaan keskenään yhden kierroksen."""
    print("He tuijottavat toisiaan...", end='')
    time.sleep(1)


    katse1 = random.randint(0, olio1.hae_katseen_voima())
    katse2 = random.randint(0, olio2.hae_katseen_voima())
    rapayttaja = None

    if katse1 > katse2:
        rapayttaja = olio2
        rapayttaja.aseta_rohkeus(rapayttaja.hae_rohkeus() - katse1)
    elif katse1 < katse2:
        rapayttaja = olio1
        rapayttaja.aseta_rohkeus(rapayttaja.hae_rohkeus() - katse2)
    return rapayttaja

def taistele(vasen, oikea):
    """Asettaa annetut oliot taistelemaan keskenään, kunnes toinen voittaa."""
    while vasen.hae_rohkeus() > 0 and oikea.hae_rohkeus() > 0:
        haviaja = tuijota(vasen, oikea)
        tulosta_rapaytys(haviaja)
        time.sleep(0.5)
    if vasen.hae_rohkeus() > 0:
        return vasen
    else:
        return oikea

def luo_satunnainen_peikko():
    """Luo satunnaisen peikkotyypin."""
    peikko_tyyppi = random.choice([Peikko, Vuorenpeikko, Luolapeikko])
    return peikko_tyyppi()

# Pääohjelma
sankari = Sankari(input("Mikä on sankarimme nimi? "))
pelastetut = 0

# Käydään tuijotuskisoja peikkoja vastaan, kunnes sankari karkaa
while sankari.hae_rohkeus() > 0:
    # Tulostetaan kierroksen alkutiedot.
    sankarin_tiedot = sankari.hae_nimi() + " [" + str(sankari.hae_rohkeus()) + "]"
    print(f"Sankarimme {sankarin_tiedot} kävelee kohti seikkailua.")
    time.sleep(0.7)

    # Luodaan satunnainen peikko ja tulostetaan sen tiedot.
    peikko = luo_satunnainen_peikko()
    peikon_tyyppi = peikko.__class__.__name__
    peikon_tiedot = peikko.hae_nimi() + " [" + str(peikko.hae_rohkeus()) + "]"
    print(f"Vastaan tulee hurja {peikon_tyyppi.lower()}: {peikon_tiedot}!")
    time.sleep(1)

    # Käydään tuijotuskisa peikkoa vastaan.
    voittaja = taistele(peikko, sankari)
    hurraa(voittaja)
    print()
    time.sleep(1.5)

time.sleep(1.5)
print(f"{sankari.hae_nimi()} herää sängystään hikisenä - onneksi se oli vain unta!")
