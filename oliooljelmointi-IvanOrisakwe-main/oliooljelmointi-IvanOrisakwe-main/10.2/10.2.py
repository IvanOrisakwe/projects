import tkinter as tk
from tkinter import ttk

class Sovellus:
    def __init__(self, root):
        self.root = root
        self.root.title("Sovellus")

        # Main container
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Left and right sections
        self.vasen = tk.Frame(self.frame, width=200, height=300)
        self.oikea = tk.Frame(self.frame, width=200, height=300, bg='red')
        self.vasen.grid(row=0, column=0, sticky='nsew')
        self.oikea.grid(row=0, column=1, sticky='nsew')

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)

        # Slider for width (10 to 50)
        self.leveys_arvo = tk.IntVar(value=50)
        self.slider = tk.Scale(self.vasen, from_=10, to=50, orient=tk.HORIZONTAL, variable=self.leveys_arvo)
        self.slider.pack(pady=5)

        # Width display label
        self.leveys_label = tk.Label(self.vasen, textvariable=self.leveys_arvo)
        self.leveys_label.pack()

        # Button to change width
        self.leveys_btn = tk.Button(self.vasen, text="Vaihda leveys", command=self.vaihda_leveys)
        self.leveys_btn.pack(expand=True)

        # Dropdown for color selection
        self.vari_valinta = tk.StringVar(value="punainen")
        self.vari_lista = ttk.Combobox(self.oikea, textvariable=self.vari_valinta,
                                       values=["punainen", "vihreä", "sininen"], state="readonly")
        self.vari_lista.pack(pady=5)

        # Button to change color
        self.vari_btn = tk.Button(self.oikea, text="Vaihda väri", command=self.vaihda_vari)
        self.vari_btn.pack(expand=True)

        # Bind Enter key to apply both actions
        self.root.bind("<Return>", self.kasittele_enter)

    def vaihda_leveys(self):
        leveys = self.leveys_arvo.get()
        self.leveys_btn.config(width=leveys)
        self.vari_btn.config(width=leveys)

    def vaihda_vari(self):
        vari = self.vari_valinta.get()
        vari_map = {
            "punainen": "red",
            "vihreä": "green",
            "sininen": "blue"
        }
        oikea_vari = vari_map.get(vari, "red")  # default to red if invalid
        self.oikea.config(bg=oikea_vari)

    def kasittele_enter(self, event):
        self.vaihda_leveys()
        self.vaihda_vari()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    Sovellus(root)
    root.mainloop()
