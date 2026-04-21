# otukset.py
# Creatures that live in the cave; depends on alkukantaiset_objektit.Otus

from alkukantaiset_objektit import Otus

class Hahmo(Otus):
    """Player character; only this class is allowed to move."""
    MERKKI = '@'

    def __init__(self, nimi: str):
        super().__init__()
        self.__nimi = nimi

    def get_name(self) -> str:
        return self.__nimi

    def move(self, dx: int, dy: int, bounds: int) -> None:
        """Move by (dx, dy) but stay within [0, bounds-1]."""
        x, y = self.get_pos()
        nx = min(max(0, x + (dx or 0)), bounds - 1)
        ny = min(max(0, y + (dy or 0)), bounds - 1)
        if nx != x or ny != y:
            self._set_pos(nx, ny)


class Bugi(Otus):
    """Bug; position is set at creation, no public movement."""
    MERKKI = 'B'

    def __init__(self, x: int, y: int):
        super().__init__()
        self._set_pos(x, y)
