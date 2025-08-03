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


    
