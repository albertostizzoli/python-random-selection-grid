import tkinter as tk
import random
import math

# lista di nomi e cognomi
names = [
    "Alberto Stizzoli", "Mekki Ouertani", "Simone Negrisoli", "Francesco Carrara", "Luca Masera",
    "Stefano Zidda", "Mirko Marasco", "Vinicius De Miranda", "Oder Risi", "Massimiliano Gilli",
    "Iacopo de Palatis", "Davide Lunetta", "Riccardo Cracolici", "Alexandru Marian Raduca", "Davide Gila",
    "Federico Manni", "Augusto Marzo", "Michele Ebau", "Matteo Pupino", "Matteo Tuveri", 
    "Cristian Ursino", "Valerio Bartoletti", "Giulia Baratella", "Daniele Giuntoli", "Riccardo Potalivo",
    "Chiara Cesari", "Erica Ostini", "Mahdi Nasser", "Giulia Mariano", "Matteo Bonelli", 
    "Giorgio Bolzoni", "Leonardo Mastrangelo", "Giovanni Megliola", "Chiara Pontello"
]

COLUMNS = 5
ROWS = math.ceil(len(names) / COLUMNS)  # calcolo dinamico delle righe necessarie

class App: 
    def __init__(self, root):
        self.root = root
        self.root.title("Selezione Alunni Classe 107") 

        self.labels = []
        self.running = False
        self.delay = 100
        
        self.frame_grid = tk.Frame(root, bg="#3C52E4")
        self.frame_grid.pack(pady=20)
        self.root.configure(bg="#3C52E4")

        # Creazione dinamica delle celle solo per i nomi esistenti
        for i in range(ROWS):
            row = []
            for j in range(COLUMNS):
                idx = i * COLUMNS + j
                if idx >= len(names):
                    break
                name = names[idx]
                lbl = tk.Label(self.frame_grid, text=name, width=22, height=3, relief="solid",
                               bg="#7FBDF7", font=("Arial", 12))
                lbl.grid(row=i, column=j, padx=5, pady=5)
                row.append(lbl)
            self.labels.append(row)

        self.btn = tk.Button(root, text="🎲 Seleziona Alunno", command=self.start_animation,
                             width=22, height=2, bg="white", font=("Arial", 12))
        self.btn.pack(pady=20)

        self.selected_label = tk.Label(root, text="", font=("Arial", 14), bg="#3C52E4", fg="white")
        self.selected_label.pack(pady=10)

    def start_animation(self):
        if self.running:
            return
        self.selected_label.config(text="")
        self.running = True
        turns = random.randint(30, 50)
        tot_cells = len(names)  # numero totale di nomi
        self.sequence = [random.randint(0, tot_cells - 1) for _ in range(turns)]
        self.delays = [int(20 + (i**1.5)) for i in range(len(self.sequence))]
        self.animate()

    def animate(self):
        if not self.sequence:
            self.running = False
            return
        index = self.sequence.pop(0)
        delay = self.delays.pop(0)
        row = index // COLUMNS
        col = index % COLUMNS

        # reset dei colori
        for r in self.labels:
            for lbl in r:
                lbl.config(bg="#7FBDF7") 
        
        # evidenzia la cella selezionata
        self.labels[row][col].config(bg="white")

        if not self.sequence:
            self.running = False
            self.flash_count = 0
            self.final_cell = self.labels[row][col]
            selected_name = self.final_cell.cget("text")
            self.selected_label.config(text=f"🎉 Selezionato: {selected_name} 🎉")
            self.flash_winner()
        else:
            self.root.after(delay, self.animate)

    def flash_winner(self):
        current_bg = self.final_cell.cget("bg")
        new_bg = "white" if current_bg == "#00ea5a" else "#00ea5a"
        self.final_cell.config(bg=new_bg)
        self.flash_count += 1
        if self.flash_count < 10:
            self.root.after(300, self.flash_winner)

# Avvio applicazione
root = tk.Tk()
app = App(root)
root.mainloop()
