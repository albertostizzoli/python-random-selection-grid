import tkinter as tk # importo tkinter per l'interfaccia
import random # importo random per la selezione casuale

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

# configuro la griglia in 5 righe e 5 colonne
ROWS = 5
COLUMNS = 5

# creo una classe per l'applicazione
class App: 
    def __init__(self, root):
        self.root = root # inizializzo la finestra principale
        self.root.title("Selezione Alunni Classe 107") 

        self.labels = [] # lista per memorizzare i nomi
        self.index_list = 0 # lista per tenere traccia degli indici selezionati
        self.running = False # variabile per controllare se il processo è in esecuzione
        self.delay = 100  # millisecondi tra le selezioni
        
        self.frame_grid = tk.Frame(root, bg="#3C52E4")  # frame per la griglia
        self.frame_grid.pack()
        self.root.configure(bg="#3C52E4")  # sfondo finestra principale

        # ciclo per creare le etichette nelle righe della griglia
        for i in range(ROWS):
            row = [] # lista per la riga corrente

            # ciclo per creare le etichette nelle colonne della griglia
            for j in range(COLUMNS):
                idx = i * COLUMNS + j # calcolo l'indice del nome
                name = names[idx] if idx < len(names) else "" # ottengo il nome corrispondente
                lbl = tk.Label(self.frame_grid, text=name, width=22, height=3, relief="solid", bg="#7FBDF7", font=("Arial", 12)) # creo l'etichetta
                lbl.grid(row= i, column=j, padx=5, pady=5) # posiziona l'etichetta nella griglia
                row.append(lbl) # aggiungo l'etichetta alla riga corrente
            self.labels.append(row) # aggiungo la riga alla lista delle etichette

        self.btn = tk.Button(root, text="🎲 Seleziona Alunno", command=self.start_animation, width=22, height=2, bg ="white", font=("Arial", 12)) # pulsante per avviare
        self.btn.pack(pady=20) # aggiungo il pulsante per avviare la selezione
        self.selected_label = tk.Label(root, text="", font=("Arial", 14), bg="#3C52E4", fg="white")
        self.selected_label.pack(pady=10)


    # creo una funzione per avviare l'animazione
    def start_animation(self):
        if self.running:
            return
        self.selected_label.config(text="")  # Pulisce il nome selezionato precedente
        self.running = True
        turns = random.randint(30, 50)
        tot_cells = ROWS * COLUMNS # calcolo il numero totale di celle
        self.sequence = [random.randint(0, tot_cells - 1) for _ in range(turns)] # genera una lista di indici casuali

        # avviene un ritardo crescente per ogni selezione tra i 20 e i 1000 millisecondi
        self.delays = [int(20 + (i**1.5)) for i in range(len(self.sequence))]

        self.animate() # avvio animazione con la funzione animate

    # creo una funzione per generare la sequenza di indici dei nomi
    def generate_sequence(self):
        turns = random.randint(30, 50) # numero di selezioni casuali
        tot_cells = ROWS * COLUMNS # calcolo il numero totale di celle
        return [random.randint(0, tot_cells - 1) for _ in range(turns)] # genera una lista di indici casuali
    
    # creo una funzione per animare la selezione
    def animate(self):
        if not self.sequence:
            self.running = False
            return
        index = self.sequence.pop(0) # ottengo l'indice della prossima selezione
        delay = self.delays.pop(0) # ottengo il ritardo per questa selezione
        row = index // COLUMNS # calcolo la riga dell'indice
        col = index % COLUMNS # calcolo la colonna dell'indice

        # resetto il colore di tutte le etichette
        for r in self.labels:
            for lbl in r:
                lbl.config(bg="#7FBDF7") 
        
        # evidenzio l'etichetta selezionata
        self.labels[row][col].config(bg="white")

        if not self.sequence:
           self.running = False # termina l'animazione
           self.flash_count = 0 # contatore per il lampeggio
           self.final_cell = self.labels[row][col] # cella finale selezionata
           # Mostra subito il nome selezionato
           selected_name = self.final_cell.cget("text")
           self.selected_label.config(text=f"🎉 Selezionato: {selected_name} 🎉")
           self.flash_winner() # evidenzio la cella vincente
        else:
           self.root.after(delay, self.animate) # chiamo ricorsivamente la funzione animate per la prossima selezione

    # creo una funzione per evidenziare la cella vincente
    def flash_winner(self):
    # viene alternato un colore tra il bianco e il verde
       current_bg = self.final_cell.cget("bg") # colore attuale
       new_bg = "white" if current_bg == "#00ea5a" else "#00ea5a" 
       self.final_cell.config(bg=new_bg)

       self.flash_count += 1 # contatore incrementato
       if self.flash_count < 10:
          self.root.after(300, self.flash_winner)


# creo la finestra principale e inizializzo l'applicazione

root = tk.Tk() # creo la finestra principale
app = App(root) # inizializzo l'applicazione
root.mainloop() # avvio l'applicazione


    
