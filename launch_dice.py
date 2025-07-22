import random # Importo la libreria random per generare numeri casuali
import tkinter as tk # Imprto la libreria tkinter per l'interfaccia grafica

# Funzione per lanciare i dadi
def lancia_dadi():
    # Prendo il numero scritto nella casella
    testo = casella_input.get()
    
    try:
        numero_dadi = int(testo)  # Converto il testo in numero intero

        if numero_dadi <= 1:
            etichetta_risultato.config(text="Inserisci un numero maggiore di 1.")
            return

        # Creo una lista con numeri casuali da 1 a 6
        risultati = []
        for _ in range(numero_dadi):
            dado = random.randint(1, 6)
            risultati.append(dado)

        # Mostro il risultato
        testo_risultato = "Risultati: " + ", ".join(str(d) for d in risultati)
        etichetta_risultato.config(text=testo_risultato)

    except ValueError:
        etichetta_risultato.config(text="Per favore, inserisci un numero valido.")


# Inizializzo la finestra principale
finestra = tk.Tk()
finestra.title("Lancio dei Dadi") # Titolo della finestra
finestra.geometry("500x500") # Dimesioni della finestra

# Titolo
etichetta_benvenuto = tk.Label(finestra, text="LANCIA I DADI 🎲", font=("Arial", 14))
etichetta_benvenuto.pack(pady=10)

# Casella di input
casella_input = tk.Entry(finestra)
casella_input.pack()
casella_input.insert(0, "2")  # Valore iniziale di default

# Pulsante per lanciare i dadi
pulsante_lancia = tk.Button(finestra, text="Lancia!", command=lancia_dadi)
pulsante_lancia.pack(pady=10)

# Etichetta dove mostro i risultati
etichetta_risultato = tk.Label(finestra, text="", font=("Arial", 12))
etichetta_risultato.pack()

# Avvio della finestra
finestra.mainloop()


