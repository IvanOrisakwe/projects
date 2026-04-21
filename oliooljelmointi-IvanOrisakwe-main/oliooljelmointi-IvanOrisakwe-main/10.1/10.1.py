import tkinter as tk

class Laskin:
    def __init__(self, root):
        self.root = root
        self.root.title("Laskin")

        self.arvo = 0  # Initial value shown

        self.syote = tk.Entry(root)
        self.syote.pack()


        self.lisaa_btn = tk.Button(root, text="Lisää lukuun", command=self.lisaa)
        self.lisaa_btn.pack()


        self.vahenna_btn = tk.Button(root, text="Vähennä luvusta", command=self.vahenna)
        self.vahenna_btn.pack()

        self.kerro_btn = tk.Button(root, text="Kerro luku", command=self.kerro)
        self.kerro_btn.pack()

        self.jaa_btn = tk.Button(root, text="Jaa luku", command=self.jaa)
        self.jaa_btn.pack()


        self.tulos = tk.Label(root, text=str(self.arvo))
        self.tulos.pack()

    def hae_syote(self):
        try:
            return float(self.syote.get())
        except ValueError:
            return 0  # Default to 0 if input is invalid

    def paivita_tulos(self):
        self.tulos.config(text=str(self.arvo))

    def lisaa(self):
        self.arvo += self.hae_syote()
        self.paivita_tulos()

    def vahenna(self):
        self.arvo -= self.hae_syote()
        self.paivita_tulos()

    def kerro(self):
        self.arvo *= self.hae_syote()
        self.paivita_tulos()

    def jaa(self):
        syote = self.hae_syote()
        if syote != 0:
            self.arvo /= syote
        else:
            self.arvo = "Virhe: 0 jako"  # Show error message
        self.paivita_tulos()

root = tk.Tk()
app = Laskin(root)
root.mainloop()
