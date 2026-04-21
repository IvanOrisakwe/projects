# alkukantaiset_objektit.py
# Base entities and cave; no print()/input(), used by the prompt API game.

class Luola:
    """Cave grid: stores exploration mask and overlays actors at render time."""
    __OUTO = '#'
    __TUTTU = '.'

    def __init__(self, koko: int):
        self.__koko = koko
        # Exploration mask only (actors are not written into this grid)
        self.__ruudut = [[self.__OUTO for _ in range(koko)] for _ in range(koko)]
        self.__otukset = []  # list of Otus

    # --- API ---
    def get_size(self) -> int:
        return self.__koko

    def add_otus(self, otus: "Otus") -> None:
        self.__otukset.append(otus)

    def remove_otus(self, otus: "Otus") -> None:
        if otus in self.__otukset:
            self.__otukset.remove(otus)

    def tutki(self, x: int, y: int) -> None:
        """Mark current tile and neighbors as explored."""
        for rivi in (y - 1, y, y + 1):
            if not (0 <= rivi < self.__koko):
                continue
            for sarake in (x - 1, x, x + 1):
                if not (0 <= sarake < self.__koko):
                    continue
                self.__ruudut[rivi][sarake] = self.__TUTTU

    def render(self) -> str:
        """Return exploration grid with actors overlaid on explored tiles."""
        rows = [list(r) for r in ("".join(r) for r in self.__ruudut)]
        for o in self.__otukset:
            ox, oy = o.get_pos()
            if 0 <= oy < self.__koko and 0 <= ox < self.__koko:
                if self.__ruudut[oy][ox] == self.__TUTTU:
                    rows[oy][ox] = o.get_mark()
        return "\n".join("".join(r) for r in rows)

    # Optional helpers
    def tile_is_explored(self, x: int, y: int) -> bool:
        return self.__ruudut[y][x] == self.__TUTTU

    def get_unknown_char(self) -> str:
        return self.__OUTO

    def get_known_char(self) -> str:
        return self.__TUTTU


class Otus:
    """Base class for any creature in the cave (encapsulated position)."""
    MERKKI = None  # subclasses must set

    def __init__(self):
        self.__x = 0
        self.__y = 0

    # Read-only public API
    def get_pos(self):
        return self.__x, self.__y

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def get_mark(self) -> str:
        return self.MERKKI

    # Protected: usable by subclasses to set position
    def _set_pos(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y
