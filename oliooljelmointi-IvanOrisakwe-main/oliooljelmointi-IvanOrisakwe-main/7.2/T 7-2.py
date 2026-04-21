
"""
Bug Hunt - Prompt API version (encapsulated)

Controls:
  • Arrow keys: move '@'
  • ESC: quit

Uses prompt.py (read, write, clear, size, KEY_*).
All attributes are private; access only via methods.
- Otus (base) has position but no public movement.
- Bugi cannot move.
- Hahmo can move via move() with bounds checking.
"""

import random
from prompt import read, write, clear, size, KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT


class Luola:
    """Represents the cave grid and manages explored tiles + actor overlay."""
    __OUTO = '#'
    __TUTTU = '.'

    def __init__(self, koko: int):
        self.__koko = koko
        # exploration mask only (no actor glyphs in the grid itself)
        self.__ruudut = [[self.__OUTO for _ in range(koko)] for _ in range(koko)]
        self.__otukset = []  # private list of actors


    def get_size(self) -> int:
        return self.__koko

    def add_otus(self, otus: "Otus") -> None:
        self.__otukset.append(otus)

    def remove_otus(self, otus: "Otus") -> None:
        if otus in self.__otukset:
            self.__otukset.remove(otus)

    def list_bugs(self):
        """Iterator over Bug objects (read-only exposure)."""
        for o in self.__otukset:
            if isinstance(o, Bugi):
                yield o

    def get_player(self) -> "Hahmo":
        for o in self.__otukset:
            if isinstance(o, Hahmo):
                return o
        raise RuntimeError("Player not found")

    def tutki(self, x: int, y: int) -> None:
        """Mark current tile and its neighbors explored."""
        for rivi in (y - 1, y, y + 1):
            if rivi < 0 or rivi >= self.__koko:
                continue
            for sarake in (x - 1, x, x + 1):
                if sarake < 0 or sarake >= self.__koko:
                    continue
                self.__ruudut[rivi][sarake] = self.__TUTTU

    def render(self) -> str:
        """Return cave with overlays. Actors appear only on explored tiles."""
        # Start from exploration mask
        rows = [list(r) for r in ("".join(r) for r in self.__ruudut)]
        # Overlay actors where explored
        for o in self.__otukset:
            ox, oy = o.get_pos()
            if 0 <= oy < self.__koko and 0 <= ox < self.__koko:
                if self.__ruudut[oy][ox] == self.__TUTTU:
                    rows[oy][ox] = o.get_mark()
        return "\n".join("".join(r) for r in rows)

    def tile_is_explored(self, x: int, y: int) -> bool:
        return self.__ruudut[y][x] == self.__TUTTU

    def get_unknown_char(self) -> str:
        return self.__OUTO

    def get_known_char(self) -> str:
        return self.__TUTTU


class Otus:
    """Base class for any creature in the cave (position is encapsulated)."""
    MERKKI = None

    def __init__(self):
        self.__x = 0
        self.__y = 0


    def get_pos(self):
        return self.__x, self.__y

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def get_mark(self) -> str:
        return self.MERKKI


    def _set_pos(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y


class Hahmo(Otus):
    """Player character that is allowed to move."""
    MERKKI = '@'

    def __init__(self, nimi: str):
        super().__init__()
        self.__nimi = nimi

    def get_name(self) -> str:
        return self.__nimi

    # Public movement method (Otus/Bugi don't have this)
    def move(self, dx: int, dy: int, bounds: int) -> None:
        """Move by (dx, dy) within [0, bounds-1]."""
        x, y = self.get_pos()
        nx = min(max(0, x + (dx or 0)), bounds - 1)
        ny = min(max(0, y + (dy or 0)), bounds - 1)
        # Only actually move if position changes (stays within bounds)
        if nx != x or ny != y:
            self._set_pos(nx, ny)


class Bugi(Otus):
    """Bug; has a position but no public movement."""
    MERKKI = 'B'

    def __init__(self, x: int, y: int):
        super().__init__()
        # Only set once at creation; no movement API exposed
        self._set_pos(x, y)


class Peli:
    """Handles game logic while keeping state private and using methods."""
    def __init__(self, koko: int, bugeja: int):
        self.__koko = koko
        self.__luola = Luola(koko)

        self.__hahmo = Hahmo('foo')
        self.__luola.add_otus(self.__hahmo)

        self.__bugit = []  # private list to track bugs separately if needed
        for _ in range(bugeja):
            self.__lisaa_bugi()

        # Explore around start
        x, y = self.__hahmo.get_pos()
        self.__luola.tutki(x, y)

        self.__siirrot = 0
        self.__hoidetut = 0

    def __lisaa_bugi(self):
        """Spawn a bug at a random tile away from (0,0)."""
        x = random.randint(1, self.__koko - 1)
        y = random.randint(1, self.__koko - 1)
        b = Bugi(x, y)
        self.__bugit.append(b)
        self.__luola.add_otus(b)

    def __debuggaa(self) -> bool:
        """Remove a bug if the player steps on it."""
        px, py = self.__hahmo.get_pos()
        for bugi in list(self.__bugit):
            bx, by = bugi.get_pos()
            if bx == px and by == py:
                self.__bugit.remove(bugi)
                self.__luola.remove_otus(bugi)
                return True
        return False

    def __sallitut_suunnat(self):
        """Compute NESW allowed directions from current player pos."""
        x, y = self.__hahmo.get_pos()
        dirs = []
        if y > 0: dirs.append('N')
        if x < self.__koko - 1: dirs.append('E')
        if y < self.__koko - 1: dirs.append('S')
        if x > 0: dirs.append('W')
        return dirs

    def draw_status(self, term_cols, top_line=0):
        status = (
            f"Find the bugs!  Moves: {self.__siirrot}   "
            f"Remaining bugs: {len(self.__bugit)}   (ESC to quit)"
        )
        write((status[:term_cols]).ljust(term_cols), top_line, 0)

    def draw_instructions(self, term_cols, top_line=1):
        msg = "Use arrow keys to move '@' and find 'B'."
        write((msg[:term_cols]).ljust(term_cols), top_line, 0)

    def draw_cave(self, top_line=2):
        cave = self.__luola.render()
        for i, row in enumerate(cave.splitlines()):
            write(row, top_line + i, 0)

    def draw_win(self, term_cols, top_line=0):
        msg = "*** All bugs squashed! Press ESC to exit. ***"
        write((msg[:term_cols]).ljust(term_cols), top_line, 0)

    def tick(self, key) -> None:
        """Handle one input step: movement + exploration + bug removal."""
        dx = dy = 0
        allowed = self.__sallitut_suunnat()
        if key == KEY_UP and 'N' in allowed:
            dy = -1
        elif key == KEY_RIGHT and 'E' in allowed:
            dx = 1
        elif key == KEY_DOWN and 'S' in allowed:
            dy = 1
        elif key == KEY_LEFT and 'W' in allowed:
            dx = -1

        if dx or dy:
            self.__hahmo.move(dx, dy, self.__koko)  # only Hahmo can move
            self.__siirrot += 1
            x, y = self.__hahmo.get_pos()
            self.__luola.tutki(x, y)
            if self.__debuggaa():
                self.__hoidetut += 1

    def is_won(self) -> bool:
        return len(self.__bugit) == 0




def game_loop(koko=10, bugeja=6):
    """Main game loop: draws, reads keys, and delegates logic to Peli."""
    clear()
    term_cols = size().columns

    peli = Peli(koko, bugeja)

    while True:
        # Draw frame
        peli.draw_status(term_cols, top_line=0)
        peli.draw_instructions(term_cols, top_line=1)
        peli.draw_cave(top_line=2)
        if peli.is_won():
            peli.draw_win(term_cols, top_line=0)

        # Read key (handle potential prefix codes on some terminals)
        key = read()
        if key in (0, 224):
            key = read()
        if key == 27:  # ESC
            break

        peli.tick(key)


if __name__ == "__main__":
    # Default: 10x10 grid with 6 bugs
    game_loop(koko=10, bugeja=6)
