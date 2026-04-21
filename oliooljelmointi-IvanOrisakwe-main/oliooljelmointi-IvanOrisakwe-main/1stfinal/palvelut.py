# palvelut.py
import random
from typing import List


class Asiakas:
    """Represents a customer with a name, internal customer number and age.

    Attributes are encapsulated (private). Use getters/setters to access them.
    """

    def __init__(self, nimi: str, ika: int) -> None:
        """Initialize with name and age; create an internal customer number."""
        self.__nimi: str = nimi
        self.__ika: int = ika
        self.__asiakasnro: List[int] = self.__luo_nro()

    # ---------- Public getters / setters ----------

    def get_nimi(self) -> str:
        """Return the customer's name."""
        return self.__nimi

    def set_nimi(self, uusi_nimi: str) -> None:
        """Set the customer's name; raise if empty/falsy."""
        if not uusi_nimi:
            raise ValueError("Anna uusi nimi.")
        self.__nimi = uusi_nimi

    def get_ika(self) -> int:
        """Return the customer's age."""
        return self.__ika

    def set_ika(self, uusi_ika: int) -> None:
        """Set the customer's age; raise if empty/falsy."""
        if not uusi_ika:
            raise ValueError("Anna uusi ikä.")
        self.__ika = uusi_ika

    def get_asiakasnro(self) -> str:
        """Return the customer number as 'XX-XXX-XXX' string."""
        a, b, c = self.__asiakasnro
        return f"{a:02}-{b:03}-{c:03}"

    # ---------- Private helpers ----------

    def __luo_nro(self) -> List[int]:
        """Create internal representation for customer number (three ints)."""
        # Two digits, then 3 digits, then 3 digits
        return [
            random.randint(0, 99),
            random.randint(0, 999),
            random.randint(0, 999),
        ]


class Palvelu:
    """Represents a service/product that can have customers."""

    def __init__(self, tuotennimi: str) -> None:
        """Initialize with product name and empty customer list."""
        self.tuotennimi: str = tuotennimi
        self.__asiakkaat: List[Asiakas] = []

    # ---------- Public API ----------

    def lisaa_asiakas(self, asiakas: Asiakas) -> None:
        """Add a customer to the service; raise if argument is falsy."""
        if not asiakas:
            raise ValueError("Anna asiakas lisättäväksi.")
        self.__asiakkaat.append(asiakas)

    def poista_asiakas(self, asiakas: Asiakas) -> None:
        """Remove the given customer; ignore if not present."""
        try:
            self.__asiakkaat.remove(asiakas)
        except ValueError:
            pass

    def tulosta_asiakkaat(self) -> None:
        """Print all customers, one per line."""
        for a in self.__asiakkaat:
            print(self._luo_asiakasrivi(a))

    # ---------- Protected helpers ----------

    def _luo_asiakasrivi(self, asiakas: Asiakas) -> str:
        """Create a printable line for a single customer."""
        return (
            f"{asiakas.get_nimi()} "
            f"({asiakas.get_asiakasnro()}) "
            f"on {asiakas.get_ika()}-vuotias"
        )


class ParempiPalvelu(Palvelu):
    """A better service that also keeps a list of benefits."""

    def __init__(self, tuotennimi: str) -> None:
        """Initialize parent and create an empty benefits list."""
        super().__init__(tuotennimi)
        self.__edut: List[str] = []

    # ---------- Public API for benefits ----------

    def lisaa_etu(self, etu: str) -> None:
        """Add a benefit; raise if argument is falsy."""
        if not etu:
            raise ValueError("Anna etu lisättäväksi.")
        self.__edut.append(etu)

    def poista_etu(self, etu: str) -> None:
        """Remove a benefit; ignore if not present."""
        try:
            self.__edut.remove(etu)
        except ValueError:
            pass

    def tulosta_edut(self) -> None:
        """Print all benefits, one per line."""
        for e in self.__edut:
            print(e)
