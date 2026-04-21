class User:
    """
    Represents a user of the bank system.

    Attributes:
        nimi (str): Name of the user.
        ika (int): Age of the user.
        sukupuoli (str): Gender.
        varat (float): Account balance.
    """
    def __init__(self, nimi, ika, sukupuoli, varat):
        self._nimi = nimi
        self._ika = ika
        self._sukupuoli = sukupuoli
        self._varat = varat

    def to_tuple(self):
        return (self._nimi, self._ika, self._sukupuoli, self._varat)

    def __str__(self):
        return f"{self._nimi}, {self._ika}, {self._sukupuoli}, {self._varat}€"
