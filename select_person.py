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
        

    
