# PYTHON-RANDOM-SELECTION-GRID

Un'applicazione desktop semplice e divertente sviluppata in **Python** con **Tkinter**, progettata per selezionare casualmente un alunno da una classe.

## 🚀 Funzionalità

- Visualizzazione di una griglia 5x5 con 34 nomi predefiniti di studenti.
- Un pulsante attiva una **selezione casuale animata** tra tutti gli studenti.
- Il nome selezionato lampeggia alla fine per attirare l'attenzione.


## 🛠️ Tecnologie utilizzate

- **Python 3**
- **Tkinter**: libreria standard per interfacce grafiche in Python.
- **Random**: per generare indici casuali e creare l'effetto lotteria.

## 🧠 Come funziona

1. L'app crea una finestra con sfondo blu e una griglia 5x5 contenente nomi.
2. Alla pressione del pulsante `🎲 Seleziona Alunno`, viene avviata un'animazione:
   - Le celle vengono evidenziate casualmente con un ritardo progressivo.
   - Una volta fermata, la cella selezionata lampeggia tra verde e bianco per evidenziare lo "studente vincitore".
   - Inoltre l'app permette di poter vedere il nome della persona selezionata sotto il pulsante.
   - Se il pulsante viene cliccato più volte il nome sparisce. 

## ▶️ Come eseguirlo

Assicurati di avere **Python 3** installato.

1. Clona o scarica il progetto.
2. Esegui il file Python:

```bash
python select_person.py
```
