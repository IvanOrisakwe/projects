

from UrllibAvustin import UrllibGet 

class WebData:
    def __init__(self, WebSivu: str):
        # Store target URL and internal caches as "private"
        self._WebSivu = WebSivu
        self._WebSisaltoRaaka = None       
        self._WebSisaltoJasennetty = None  

    def PalautaRaaka(self) -> str:
        """
        Return the page HTML as a string.
        Uses UrllibGet (returns bytes) and decodes to UTF-8 (fallback).
        """
        if self._WebSisaltoRaaka is None:
            data = UrllibGet(self._WebSivu)  
            self._WebSisaltoRaaka = (
                data.decode("utf-8", errors="replace")
                if isinstance(data, (bytes, bytearray))
                else str(data)
            )
        return self._WebSisaltoRaaka

    def PalautaJasennetty(self) -> list:
        """
        Return a parsed list by splitting the HTML string on '>'.
        (Very simple tokenizer per the assignment’s hint.)
        """
        raw = self.PalautaRaaka()
        if self._WebSisaltoJasennetty is None:
            self._WebSisaltoJasennetty = raw.split('>')
        return self._WebSisaltoJasennetty
