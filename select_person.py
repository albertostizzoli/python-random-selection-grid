import tkinter as tk
import random

# Lista di nomi e cognomi
names = [
    "Alberto Stizzoli", "Mekki Ouertani", "Simone Negrisoli", "Francesco Carrara", "Luca Masera",
    "Stefano Zidda", "Mirko Marasco", "Vinicius De Miranda", "Oder Risi", "Massimiliano Gilli",
    "Iacopo de Palatis", "Davide Lunetta", "Riccardo Cracolici", "Alexandru Marian Raduca", "Davide Gila",
    "Federico Manni", "Augusto Marzo", "Michele Ebau", "Matteo Pupino", "Matteo Tuveri", 
    "Cristian Ursino", "Valerio Bartoletti", "Giulia Baratella", "Daniele Giuntoli", "Riccardo Potalivo",
    "Chiara Cesari", "Erica Ostini", "Mahdi Nasser", "Giulia Mariano", "Matteo Bonelli", 
    "Giorgio Bolzoni", "Leonardo Mastrangelo", "Giovanni Megliola", "Chiara Pontello"
]

# Configuro la griglia
ROWS = 5
COLUMNS = 6

class App: 
    def __init__(self, root):
        self.root = root # Inizializzo la finestra principale
        self.root.title("Selezione casuale di persone") 

        self.labels = [] # Lista per memorizzare i nomi
        self.index_list = 0 # Lista per tenere traccia degli indici selezionati
        self.running = False # Variabile per controllare se il processo è in esecuzione
        self.delay = 100  # Millisecondi tra le selezioni
        
        self.frame_grid = tk.Frame(root)  # Frame per la griglia
        self.frame_grid.pack()

        # Ciclo per creare le etichette nelle righe della griglia
        for i in range(ROWS):
            row = [] # Lista per la riga corrente

            # Ciclo per creare le etichette nelle colonne della griglia
            for j in range(COLUMNS):
                idx = i * COLUMNS + j # Calcolo l'indice del nome
                name = names[idx] if idx < len(names) else "" # Ottengo il nome corrispondente
                lbl = tk.Label(self.frame_grid, text=name, width=20, height=2, relief="solid", bg="lightblue", font=("Arial", 12)) # Crea l'etichetta
                lbl.grid(row= i, column=j, padx=5, pady=5) # Posiziona l'etichetta nella griglia
                row.append(lbl) # Aggiungo l'etichetta alla riga corrente
            self.labels.append(row) # Aggiungo la riga alla lista delle etichette

        self.btn = tk.Button(root, text="🎲 Seleziona", command=self.start_animation) # Pulsante per avviare
        self.btn.pack(pady=10) # Aggiungo il pulsante per avviare la selezione)

    # creo una funzione per avviare l'animazione
    def start_animation(self):
        if self.running:
            return
        self.running = True
        turns = random.randint(30, 50)
        tot_cells = ROWS * COLUMNS # Calcolo il numero totale di celle
        self.sequence = [random.randint(0, tot_cells - 1) for _ in range(turns)] # Genera una lista di indici casuali

        # Ritardi crescenti da 20ms a circa 400ms
        self.delays = [int(20 + (i**1.5)) for i in range(len(self.sequence))]

        self.animate() # Avvia l'animazione

    # creo una funzione per generare la sequenza di indici dei nomi
    def generate_sequence(self):
        turns = random.randint(30, 50) # Numero di selezioni casuali
        tot_cells = ROWS * COLUMNS # Calcolo il numero totale di celle
        return [random.randint(0, tot_cells - 1) for _ in range(turns)] # Genera una lista di indici casuali
    
    # creo una funzione per animare la selezione
    def animate(self):
        if not self.sequence:
            self.running = False
            return
        index = self.sequence.pop(0) # Ottengo l'indice della prossima selezione
        delay = self.delays.pop(0) # Ottengo il ritardo per questa selezione
        row = index // COLUMNS # Calcolo la riga dell'indice
        col = index % COLUMNS # Calcolo la colonna dell'indice

        # Resetto il colore di tutte le etichette
        for r in self.labels:
            for lbl in r:
                lbl.config(bg="lightblue")
        
        # evidenzio l'etichetta selezionata
        self.labels[row][col].config(bg="yellow")

        if not self.sequence:
           self.running = False # termina l'animaizione
           self.flash_count = 0 # contatore per il lampeggio
           self.final_cell = self.labels[row][col] # cella finale selezionata
           self.flash_winner() # evidenzio la cella vincente
        else:
           self.root.after(delay, self.animate) # chiamo ricorsivamente la funzione animate per la prossima selezione

    # creo una funzione per evidenziare la cella vincente
    def flash_winner(self):
    # Alterna il colore tra verde e bianco
       current_bg = self.final_cell.cget("bg") # colore attuale
       new_bg = "white" if current_bg == "green" else "green"
       self.final_cell.config(bg=new_bg)

       self.flash_count += 1 # contatore incrementato
       if self.flash_count < 30:  # Numero totale di cambi colore (10 lampeggi)
        self.root.after(300, self.flash_winner)


root = tk.Tk() # Creo la finestra principale
app = App(root) # Inizializzo l'applicazione
root.mainloop() # Avvio l'applicazione


    
