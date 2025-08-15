import tkinter as tk # impoorto tkinter per l'interfaccia grafica
import random # importo random per la selezione casuale
import math # importo math per calcoli matematici

# lista di nomi e cognomi
names = [
    "Alberto Stizzoli", "Mekki Ouertani", "Simone Negrisoli", "Francesco Carrara", "Luca Masera",
    "Stefano Zidda", "Mirko Marasco", "Vinicius De Miranda", "Oder Risi", "Massimiliano Gilli",
    "Iacopo de Palatis", "Davide Lunetta", "Riccardo Cracolici", "Alexandru Marian Raduca", "Davide Gila",
    "Federico Manni", "Augusto Marzo", "Michele Ebau", "Matteo Pupino", "Matteo Tuveri", 
    "Cristian Ursino", "Valerio Bartoletti", "Chiara Pontello", "Giulia Baratella", "Daniele Giuntoli", 
    "Riccardo Potalivo", "Chiara Cesari", "Erica Ostini", "Mahdi Nasser", "Giulia Mariano", 
    "Matteo Bonelli", "Giorgio Bolzoni", "Leonardo Mastrangelo", "Giovanni Megliola"
]

# configurazione della griglia
COLUMNS = 5
ROWS = math.ceil(len(names) / COLUMNS)  # calcolo dinamico delle righe necessarie

class App: 
    def __init__(self, root): # inizializzazione dell'applicazione
        self.root = root # imposta la finestra principale
        self.root.title("Selezione Alunni Classe 107") 

        self.labels = [] # lista per memorizzare le etichette della griglia
        self.running = False # stato dell'animazione
        self.delay = 100 # ritardo tra le animazioni
        
        self.frame_grid = tk.Frame(root, bg="#3C52E4")
        self.frame_grid.pack(pady=20)
        self.root.configure(bg="#3C52E4")

        # creo dinamicamente le celle solo per i nomi esistenti
        for i in range(ROWS):
            row = []  # lista per memorizzare le etichette della riga
            for j in range(COLUMNS): # ciclo per le colonne
                idx = i * COLUMNS + j # calcolo l'indice del nome
                if idx >= len(names): # se l'indice supera il numero di nomi, esco dal ciclo
                    break
                name = names[idx] # prendo il nome dalla lista
                lbl = tk.Label(self.frame_grid, text=name, width=22, height=3, relief="solid", bg="#7FBDF7", font=("Arial", 12))
                lbl.grid(row=i, column=j, padx=5, pady=5)
                row.append(lbl) # aggiungo l'etichetta alla riga
            self.labels.append(row) # aggiungo la riga alla lista delle etichette

        # pulsante per avviare l'animazione
        self.btn = tk.Button(root, text="🎲 Seleziona Alunno", command=self.start_animation,  width=22, height=2, bg="white", font=("Arial", 12))
        self.btn.pack(pady=20)

        self.selected_label = tk.Label(root, text="", font=("Arial", 14), bg="#3C52E4", fg="white")
        self.selected_label.pack(pady=10)

    # creo una funzione per avviare l'animazione
    def start_animation(self):
        if self.running: # se l'animazione è già in corso, non faccio nulla
            return
        self.selected_label.config(text="")
        self.running = True # avvio l'animazione
        turns = random.randint(30, 50)
        tot_cells = len(names)  # numero totale di nomi
        self.sequence = [random.randint(0, tot_cells - 1) for _ in range(turns)] # creo una sequenza casuale di indici
        self.delays = [int(20 + (i**1.5)) for i in range(len(self.sequence))] # calcolo i ritardi per ogni selezione
        self.animate() # avvio l'animazione
    
    # creo una funzione per animare la selezione casuale
    def animate(self):
        if not self.sequence:
            self.running = False # se non ci sono più indici da selezionare, esco dalla funzione
            return
        index = self.sequence.pop(0) # prendo il primo indice dalla sequenza
        delay = self.delays.pop(0) # prendo il ritardo corrispondente all'indice
        row = index // COLUMNS # calcolo la riga in base all'indice
        col = index % COLUMNS # calcolo la colonna in base all'indice

        # reset dei colori
        for r in self.labels:
            for lbl in r:
                lbl.config(bg="#7FBDF7") 
        
        # evidenzia la cella selezionata
        self.labels[row][col].config(bg="white")

        if not self.sequence:
            self.running = False # se non ci sono più indici da selezionare, fermo l'animazione
            self.flash_count = 0 # inizializzo il contatore dei lampeggi
            self.final_cell = self.labels[row][col] # salvo la cella finale
            selected_name = self.final_cell.cget("text")
            self.selected_label.config(text=f"🎉 Selezionato: {selected_name} 🎉")
            self.flash_winner() # inizio il lampeggio della cella del vincitore
        else:
            self.root.after(delay, self.animate) # richiamo la funzione animate dopo il ritardo specificato

    # creo una funzione per lampeggiare la cella del vincitore
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
